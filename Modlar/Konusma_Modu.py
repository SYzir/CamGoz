from Modlar.BasicMod import Mod


class Konusma(Mod):
    def __init__(self,nesne,dogruluk):
        super().__init__()
        self.nesne = nesne
        self.dogruluk

    def goster(self):
         print("Konuşma Modu")
         print(f"Nesen = {self.nesne} / Doğruluk Değeri = {self.dogruluk}")



