from Modlar.BasicMod import Mod
import YOLO as yolo
import threading as th
import asyncio
from fastapi import WebSocket


class Yurume(Mod):
    def __init__(self,dogruluk):
        super().__init__()
        self.dogruluk = dogruluk
        self.stop_signal = False #Gelecek framelerde kullanılacak döngude durdurma flag'i
        self.th = th.Thread(target=self.walk)
        self.th.start()

    async def send_data(self,websocket: WebSocket,data):
        await websocket.send_json(data)

    def walk(self):
        async def inner_walk():
            uri = "ws://localhost:8000/ws"
            async with WebSocket.connect(uri) as websocket:
                print("Websocket bağlantısı kuruldı, Mod başlatıldı")

                while not self.stop_signal:
                    frame = await websocket.receive_json() # burada frontend den gelen json formattında receive edilecek
                    result = yolo.yolo_detect(frame)

                    if result:
                        detected_object, confidence = result
                        await self.send_data(websocket,{"detected_object ": detected_object})

                    else:
                        await self.send_data(websocket,{"detected_object ": None})
        asyncio.run(inner_walk())    

    def process(self):
        try:
            self.th.join()
        except KeyboardInterrupt:
            self.stop_signal = True
            print("Mode durduruldu")