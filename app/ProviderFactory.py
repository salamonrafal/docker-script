from app.Interfaces import ProviderFactoryInterface, ProviderInterface, ReaderInterface, WriterInterface
from app.Proviaders import Image, Container, Compose, Clean, Build, Init
from app.Exceptions import UnhandledCommandException
from app.Locale import Labels
from app.Di import SimplyDi

_CMD_NAME_DOCKER_IMAGE = "docker-image"
_CMD_NAME_DOCKER_CONTAINER = "docker-container"
_CMD_NAME_DOCKER_COMPOSE = "docker-compose"
_CMD_NAME_INIT = "init"
_CMD_NAME_BUILD = "build"
_CMD_NAME_CLEAN = "clean"
_CMD_NAME_UNHANDLED = None


class ProviderFactory(ProviderFactoryInterface):
    yaml_reader: ReaderInterface
    yaml_writer: WriterInterface
    labels: Labels
    script_path: str
    Sdi: SimplyDi
    
    def __init__(self, sdi: SimplyDi):
        self.Sdi = sdi
        self.yaml_reader = self.Sdi.get_service("yaml_reader")
        self.yaml_writer = self.Sdi.get_service("yaml_writer")
        self.labels = self.Sdi.get_service("labels")
        self.script_path = self.Sdi.get_service("script_dir_name")
        pass
    
    def register(self, provider_name: str) -> ProviderInterface:
        provider = {
            _CMD_NAME_DOCKER_IMAGE: Image(_CMD_NAME_DOCKER_IMAGE, self.Sdi),
            _CMD_NAME_DOCKER_CONTAINER: Container(_CMD_NAME_DOCKER_CONTAINER, self.Sdi),
            _CMD_NAME_DOCKER_COMPOSE: Compose(_CMD_NAME_DOCKER_COMPOSE, self.Sdi),
            _CMD_NAME_BUILD: Build(_CMD_NAME_BUILD, self.Sdi),
            _CMD_NAME_CLEAN: Clean(_CMD_NAME_CLEAN, self.Sdi),
            _CMD_NAME_INIT: Init(_CMD_NAME_INIT, self.Sdi),
            }.get(provider_name, _CMD_NAME_UNHANDLED)
        
        if provider is _CMD_NAME_UNHANDLED:
            raise UnhandledCommandException("Unhandled command {}".format(provider_name))
            
        return provider
