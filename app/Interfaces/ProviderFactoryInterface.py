from abc import abstractmethod, ABC
from app.Interfaces import ProviderInterface


class ProviderFactoryInterface(ABC):
    @abstractmethod
    def register(self, provider_name: str) -> ProviderInterface: raise NotImplementedError
