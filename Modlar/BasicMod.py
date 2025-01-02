from abc import ABC, abstractmethod

class Mod(ABC):

    @abstractmethod
    def goster(self):
        pass
    
    @abstractmethod
    def process(self):
        pass
