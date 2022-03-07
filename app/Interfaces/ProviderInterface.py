from abc import abstractmethod, ABCMeta
from app.Di import SimplyDi


class ProviderInterface:
    __metaclass__ = ABCMeta
    provider_type: str = ""
    script_path: str
    di: SimplyDi

    def __init__(self, provider_type_arg: str, di: SimplyDi):
        self.provider_type = provider_type_arg
        self.di = di
        self.script_path = di.get_service("script_dir_name")
        pass

    @abstractmethod
    def execute(self, *args) -> bool: raise NotImplementedError
