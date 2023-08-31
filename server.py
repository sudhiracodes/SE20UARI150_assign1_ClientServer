import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            response = f"Server: Hi, I'm the server!"
            await websocket.send(response)
            print(f"Sent message to client: {response}")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected.")

async def main():
    async with websockets.serve(handle_client, "139.59.33.235", 5000):
        print(f"listening")
        await asyncio.Future()
        
if __name__ == "__main__":
    asyncio.run(main())
