from abc import abstractmethod, ABC
from lib.Interfaces import ProviderInterface


class ProviderFactoryInterface(ABC):
    @abstractmethod
    def register(self, provider_name: str) -> ProviderInterface: raise NotImplementedError
