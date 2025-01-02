from Modlar.BasicMod import Mod
import threading as thr 
import asyncio 
from fastapi import WebSocket 
from tesseract import ocr_detect


class Okuma(Mod):
    def __init__(self,nesne,dogruluk):
        super().__init__()
        self.nesne = nesne
        self.dogruluk = dogruluk
        self.okunan_kelime = "There are not any string"
        
        self.thr = thr.Thread(target=self.read())
        self.thr.start()

    async def send_data(self,websocket:WebSocket,data):
        await websocket.send_json(data)
    
    def read(self):
        async def inner_read():
            uri = "ws://localhost:8000/ws"
            async with WebSocket.connect(uri) as websocket:
                while True:
                    text = ocr_detect()
                    if text:
                        await self.send_data(websocket,text)
        asyncio.run(inner_read())

    def goster(self):
        print("Okuma Modu")
        print(f"Nesen : {self.nesne} / Doğruluk değeri = {self.dogruluk}")
        print(f"okunan kelime = {self.okunan_kelime}")

