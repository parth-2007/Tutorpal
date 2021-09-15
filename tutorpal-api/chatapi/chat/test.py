from channels.testing import WebsocketCommunicator
from .consumers import ChatConsumer
import asyncio

async def test():
    communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), "/ws/chat/1/")
    connected, subprotocol = await communicator.connect()
    assert connected
    # Test sending text
    await communicator.send_to(text_data="hello")
    response = await communicator.receive_from()
    print(response)
    # Close
    await communicator.disconnect()

def main():
    asyncio.run(test())