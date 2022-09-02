from abc import ABC, abstractmethod

class EngineModel(ABC):

    @abstractmethod
    def needs_service(self):
        pass