from abc import abstractmethod, ABCMeta


class ReaderInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self, name) -> str: raise NotImplementedError
