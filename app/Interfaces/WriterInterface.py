from abc import abstractmethod, ABCMeta


class WriterInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def write(self, name) -> bool: raise NotImplementedError
