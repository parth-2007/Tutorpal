from paypalpayoutssdk.core import PayPalHttpClient, SandboxEnvironment
from paypalpayoutssdk.payouts import PayoutsPostRequest
from paypalcheckoutsdk.payments import CapturesRefundRequest
from paypalcheckoutsdk.orders import OrdersCaptureRequest
from paypalhttp import HttpError
from django.conf import settings
import os
import sys


def send_payout(email, price, session_id):
    # Creating Access Token for Sandbox
    client_id = os.environ.get('PAYPAL_CLIENT_ID')
    client_secret = os.environ.get('PAYPAL_CLIENT_SECRET')

    # Creating an environment
    environment = SandboxEnvironment(
        client_id=client_id, client_secret=client_secret)
    client = PayPalHttpClient(environment)

    body = {
        "sender_batch_header": {
            "recipient_type": "EMAIL",
            "email_message": "Your TutorPal Payment",
            "note": "This is your Tutorpal payment",
                    "sender_batch_id": f"Payout_{session_id}",
                    "email_subject": "Your TutorPal Payment"
        },
        "items": [{
            "note": "Your Payout!",
            "amount": {
                "currency": "USD",
                "value": f"{price}"
            },
            "receiver": f"{email}",
            "sender_item_id": "Test_txn_1"
        }]
    }

    request = PayoutsPostRequest()
    request.request_body(body)

    try:
        # Call API with your client and get a response for your call
        # response =
        client.execute(request)
        # If call returns body in response, you can get the deserialized version from the result attribute of the response
        # batch_id = response.result.batch_header.payout_batch_id
        # print(batch_id)
        return 'success'
    except IOError as ioe:
        print(ioe)
        if isinstance(ioe, HttpError):
            # Something went wrong server-side
            print(ioe.status_code)
        return 'error'


class PayPalClient:
    def __init__(self):
        self.client_id = os.environ.get('PAYPAL_CLIENT_ID')
        self.client_secret = os.environ.get('PAYPAL_CLIENT_SECRET')

        """Set up and return PayPal Python SDK environment with PayPal access credentials.
           This sample uses SandboxEnvironment. In production, use LiveEnvironment."""

        self.environment = SandboxEnvironment(
            client_id=self.client_id, client_secret=self.client_secret)

        """ Returns PayPal HTTP client instance with environment that has access
            credentials context. Use this instance to invoke PayPal APIs, provided the
            credentials have access. """
        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        """
        Function to print all json data in an organized readable manner
        """
        result = {}
        if sys.version_info[0] < 3:
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()
        for key, value in itr:
            # Skip internal attributes.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else\
                self.object_to_json(value) if not self.is_primittive(value) else\
                value
        return result

    def array_to_json_array(self, json_array):
        result = []
        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if not self.is_primittive(item)
                              else self.array_to_json_array(item) if isinstance(item, list) else item)
        return result

    def is_primittive(self, data):
        # return isinstance(data, str) or isinstance(data, unicode) or isinstance(data, int)
        return isinstance(data, str) or isinstance(data, int)


class CaptureOrder(PayPalClient):
    # Set up your server to receive a call from the client
    """this sample function performs payment capture on the order.
    Approved order ID should be passed as an argument to this function"""

    def capture_order(self, order_id):
        """Method to capture order using order_id"""
        request = OrdersCaptureRequest(order_id)
        # Call PayPal to capture an order
        response = self.client.execute(request)
        # Save the capture ID to your database. Implement logic to save capture to your database for future reference.
        if settings.DEBUG:
            print('Status Code: ', response.status_code)
            print('Status: ', response.result.status)
            print('Order ID: ', response.result.id)
            print('Links: ')
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(
                    link.rel, link.href, link.method))
            print('Capture Ids: ')
            for purchase_unit in response.result.purchase_units:
                for capture in purchase_unit.payments.captures:
                    print('\t', capture.id)
        return response


def capture_order(order_id):
    return CaptureOrder().capture_order(order_id)


class RefundOrder(PayPalClient):

    # Set up your server to receive a call from the client
    """Use the following function to refund an capture.
       Pass a valid capture ID as an argument."""

    def refund_order(self, capture_id, amount):
        request = CapturesRefundRequest(capture_id)
        request.prefer("return=representation")
        request.request_body(self.build_request_body(amount))
        # Call PayPal to refund an capture
        response = self.client.execute(request)
        if settings.DEBUG:
            print('Status Code:', response.status_code)
            print('Status:', response.result.status)
            print('Order ID:', response.result.id)
            print('Links:')
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(
                    link.rel, link.href, link.method))
            # json_data = self.object_to_json(response.result)
            # print("json_data: ", json.dumps(json_data, indent=4))
        return response

    """Request body for building a partial refund request.
     For full refund, pass the empty body.
     For more details, refer to the Payments API refund captured payment reference."""
    @staticmethod
    def build_request_body(amount):
        return \
            {
                "amount": {
                    "value": str(amount),
                    "currency_code": "USD"
                }
            }


def refund_order(capture_id, amount):
    RefundOrder().refund_order(capture_id, amount)
