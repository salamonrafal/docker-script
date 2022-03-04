from app.Annotations import param_shorts, ShortAliases


@param_shorts
class Parameters(ShortAliases):
    command: str = None
    image_name: str = None
    docker_file: str = None
    version: str = None
    action: str = None
    environment: str = None

    def __init__(
        self,
        command: str = "",
        image_name: str = "",
        docker_file: str = "Dockerfile",
        version: str = "",
        action: str = "",
        environment: str = ""
    ):
        self.__update(command, image_name, docker_file, version, action, environment)
        pass
    
    def __update(
            self,
            command: str,
            image_name: str,
            docker_file: str,
            version: str,
            action: str,
            environment: str
    ):
        self.image_name = image_name
        self.docker_file = docker_file
        self.version = version
        self.command = command
        self.action = action
        self.environment = environment
        pass

    # image_name: i
    def get_image_name(self) -> str: return self.image_name

    # docker_file: d
    def get_docker_file(self) -> str: return self.docker_file

    # version: vd
    def get_version(self) -> str: return self.version

    # command: c
    def get_command(self) -> str: return self.command

    # action: a
    def get_action(self) -> str: return self.action

    # environment: e
    def get_environment(self) -> str: return self.environment
