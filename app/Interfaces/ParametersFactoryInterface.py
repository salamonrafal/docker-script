from abc import abstractmethod, ABCMeta
from app.Models.Parameters import Parameters


class ParametersFactoryInterface:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def prepare_parameters(self, argv) -> Parameters: raise NotImplementedError
