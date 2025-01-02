from BaseFactory import factory
from Modlar.Konum_Modu import Konum
from Modlar.Konusma_Modu import Konusma
from Modlar.Yurume_Modu import Yurume
from Modlar.OkumaModu import Okuma
import YOLO as yolo

from fastapi import FastAPI, WebSocket
import threading as thr

app = FastAPI()
fac = factory()

@app.get("/mode/{choice}")
def get_mode(choice: str):
    mode = fac.getMode(choice)

    if mode:
        mode.goster()
        thr.Thread(target=mode.process).start()
        return {"message":f"{choice} modu aktif"}
    else:
        return {"message":f"Geçersiz mod :{choice}"}
    
async def websocket_endpoint(websocket : WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send_json(f"Received : {data}")
