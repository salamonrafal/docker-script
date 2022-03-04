from abc import abstractmethod, ABCMeta


class ValidatorInterface:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def validate(self): raise NotImplementedError
