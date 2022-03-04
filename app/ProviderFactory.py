from app.Interfaces import ProviderFactoryInterface, ProviderInterface
from app.Docker import Image, Container, Compose
from app.Exceptions import UnhandledCommandException


class ProviderFactory(ProviderFactoryInterface):
    def register(self, provider_name: str) -> ProviderInterface:
        provider = {
            "docker-image": Image("docker-image"),
            "docker-container": Container("docker-container"),
            "docker-compose": Compose("docker-compose")
            }.get(provider_name, None)
        
        if provider is None:
            raise UnhandledCommandException("Unhandled command {}".format(provider_name))
            
        return provider
