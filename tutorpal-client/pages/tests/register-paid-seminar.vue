<template>
  <div>
    <body>
      <div ref="paypal"></div>
      <!-- <button @click="sendRequest">register for a paid seminar</button> -->
      <pre>{{ data }}</pre>
    </body>
  </div>
</template>
<script>
import getCSRF from '~/utils/getCSRF'
export default {
  data() {
    return {
      data: '',
    }
  },
  mounted() {
    const script = document.createElement('script')
    script.src = // using the dev one
      'https://www.paypal.com/sdk/js?client-id=AWW16XfjrRH_ES95pba-gKzG2Zf51wsnFT00MqTASBMYetPIoGvo9zjAH2_K5yZ9rW3ssiwGXqsHl1iJ&enable-funding=venmo&currency=USD'
    script.addEventListener('load', this.setLoaded)
    document.body.appendChild(script)
  },
  methods: {
    setLoaded() {
      window.paypal
        .Buttons({
          style: {
            color: 'blue',
            shape: 'pill',
            label: 'pay',
            height: 40,
          },
          createOrder: (data, actions) => {
            return actions.order.create({
              purchase_units: [
                {
                  amount: {
                    currency_code: 'USD',
                    value: parseFloat(2.5), // fix price
                  },
                },
              ],
            })
          },
          onApprove: async (data, actions) => {
            const csrfToken = await getCSRF()
            const respData = await fetch(
              process.env.API_URL + '/seminars/23/register/',
              {
                method: 'POST',
                credentials: 'include',
                headers: {
                  'X-CSRFToken': csrfToken.success,
                  'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                  order_id: data.orderID,
                }),
              }
            ).then((res) => res.json())
            this.data = respData
            return actions.order.capture().then(function (orderData) {
              console.log(
                'Capture result',
                orderData,
                JSON.stringify(orderData, null, 2)
              )
            })
          },
        })
        .render(this.$refs.paypal)
    },
  },
}
</script>
<style scoped>
.badge {
  position: absolute;
  top: 11px;
  right: 3px;
  padding: 4px 7px;
  border-radius: 1000px;
  background-color: red;
  color: white;
  font-family: Poppins;
  font-size: 14px;
}
</style>