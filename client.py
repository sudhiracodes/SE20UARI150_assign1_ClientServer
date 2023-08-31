import asyncio
import websockets

async def send_and_receive():
    try:
        uri = "ws://139.59.33.235:5000"  # Replace with your cloud server's IP and port
        async with websockets.connect(uri) as websocket:
            message = "Hi, I'm the client,sudhira!"
            await websocket.send(message)
            print(f"Sent message to server: {message}")

            response = await websocket.recv()
            print(f"Received message from server: {response}")
    except websockets.exceptions.ConnectionClosed:
        print("Connection to server closed.")

async def main():
    await send_and_receive()

asyncio.run(main())
