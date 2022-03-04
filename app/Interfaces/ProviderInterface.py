from abc import abstractmethod, ABCMeta


class ProviderInterface:
    __metaclass__ = ABCMeta
    provider_type: str = ""

    def __init__(self, provider_type_arg: str):
        self.provider_type = provider_type_arg
        pass

    @abstractmethod
    def execute(self, *args) -> bool: raise NotImplementedError
