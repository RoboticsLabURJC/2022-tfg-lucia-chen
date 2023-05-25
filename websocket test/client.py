import asyncio
from websockets.sync.client import connect

def hello():
    with connect("ws://localhost:8765") as websocket:
        websocket.send("Hola servidor!")
        message = websocket.recv()
        print(f"Mensaje recibido: {message}")

hello()