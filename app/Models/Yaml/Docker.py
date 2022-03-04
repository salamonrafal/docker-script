from app.Models.Yaml import YamlObject

class Docker(YamlObject):
    docker_file: str = 'Dockerfile'
    environment: str = 'production'
    image_name: str = 'app'
    version: str = ''
    prefix_name: str = 'app-service-'
    containers_name: str = "web,app"
    
    def __init__(self,
        docker_file: str = None,
        environment: str = None,
        image_name: str = None,
        version: str = None,
        prefix_name: str = None,
        containers_name: str = None
    ):
        if docker_file is not None: self.docker_file = docker_file
        if environment is not None: self.environment = environment
        if image_name is not None: self.image_name = image_name
        if version is not None: self.version = version
        if prefix_name is not None: self.prefix_name = prefix_name
        if containers_name is not None: self.containers_name = containers_name
        
        pass
    
    def to_dict(self) -> dict: return {
        "docker_file": self.docker_file,
        "environment": self.environment,
        "image_name": self.image_name,
        "version": self.version,
        "prefix_name": self.prefix_name,
        "containers_name": self.containers_name,
    }
    