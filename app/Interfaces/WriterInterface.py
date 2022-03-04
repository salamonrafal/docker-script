from abc import abstractmethod, ABCMeta


class WriterInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def write(self, name: str, data) -> bool: raise NotImplementedError
