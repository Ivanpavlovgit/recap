from abc import ABC,abstractmethod

class Repository(ABC):
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def write(self):
        pass

