from Modlar.Konum_Modu import Konum
from Modlar.Konusma_Modu import Konusma
from Modlar.Yurume_Modu import Yurume
from Modlar.OkumaModu import Okuma

class FactoryExecption(Exception):
    pass

class factory:
    choice = "MOD_YOK"

    def getMode(self,choice):
        try:            
            self.choice = choice
            if (choice == "SAĞA"):
                walk = Yurume(0.7)
                return walk 
            
            elif (choice == "SOLA"):#bu konum modu şuan yanlis düzeltilecek 
                place = Konum()
                return place

            elif (choice == "YUKARI"):
                speak = Konusma("person",85)
                return speak

            elif (choice == "AŞAĞI"):
                read = Okuma("book",0.95)
                return read
            
            else:
                raise FactoryExecption(f"gecersiz mod secimi: {choice}")
        
        except FactoryExecption as e:
            print(f"Hata : {e}")
            return None               
    
    def diplay(self):
        print(self.choice)