from Modlar.BasicMod import Mod
import YOLO as yolo
import threading as th
import asyncio
from fastapi import WebSocket


class Yurume(Mod):
    def __init__(self,dogruluk):
        super().__init__()
        self.dogruluk = dogruluk
        self.th = th.Thread(target=self.walk)
        self.th.start()

    async def send_data(self,websocket: WebSocket,data):
        await websocket.send_json(data)

    def walk(self):
        async def inner_walk():
            uri = "ws://localhost:8000/ws"
            async with WebSocket.connect(uri) as websocket:
                while True:
                    result = yolo.yolo_detect()
                    await self.send_data(websocket,result)
        asyncio.run(inner_walk())    

    def goster(self):
        print("Yurume Modu")
        print(f"Doğruluk Değeri = {self.dogruluk}")

    def process(self):
        self.th.join()