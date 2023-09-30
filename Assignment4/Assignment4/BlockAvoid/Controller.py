from abc import ABC, abstractmethod
class Controller(ABC):
    """description of class"""
    @abstractmethod
    def handleEvent(self,event):
        pass

