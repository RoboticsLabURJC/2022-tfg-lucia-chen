import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        print(f"Mensaje recibido: {message}")
        await websocket.send("Hola cliente!")

async def main():
    async with serve(echo, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
