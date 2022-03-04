from app.Annotations import param_shorts, ShortAliases


@param_shorts
class Parameters(ShortAliases):
    command: str = None
    image_name: str = None
    docker_file: str = None
    version: str = None
    action: str = None
    environment: str = None
    container_name: str = None
    silent: bool

    def __init__(
        self,
        command: str = "",
        image_name: str = "",
        docker_file: str = "",
        version: str = "",
        action: str = "",
        environment: str = "",
        container_name: str = "",
        silent: bool = False
    ):
        super(Parameters, self).__init__()
        
        self.__update(
            command,
            image_name,
            docker_file if docker_file != "" else "Dockerfile",
            version,
            action,
            environment,
            container_name,
            silent
        )
        pass
    
    def __update(
        self,
        command: str,
        image_name: str,
        docker_file: str,
        version: str,
        action: str,
        environment: str,
        container_name: str,
        silent: bool
    ):
        self.image_name = image_name
        self.docker_file = docker_file
        self.version = version
        self.command = command
        self.action = action
        self.environment = environment
        self.container_name = container_name
        self.silent = silent
        pass

    # image_name: i
    def get_image_name(self) -> str: return self.image_name
    def set_image_name(self, image_name: str): self.image_name = image_name
    
    # container_name: cn
    def get_container_name(self) -> str: return self.container_name
    def set_container_name(self, container_name: str): self.container_name = container_name

    # docker_file: d
    def get_docker_file(self) -> str: return self.docker_file
    def set_docker_file(self, docker_file: str): self.docker_file = docker_file

    # version: vd
    def get_version(self) -> str: return self.version
    def set_version(self, version: str): self.version = version

    # command: c
    # cache build: image_name,docker_file,version,environment
    def get_command(self) -> str: return self.command
    def set_command(self, command: str): self.command = command

    # action: a
    def get_action(self) -> str: return self.action
    def set_action(self, action: str): self.action = action

    # environment: e
    def get_environment(self) -> str: return self.environment
    def set_environment(self, environment: str): self.environment = environment
    
    # silent: s
    def get_silent(self) -> bool: return self.silent
    def set_silent(self, silent: bool): self.silent = silent
    
    def __getitem__(self, item):
        if item == "image_name":
            return self.get_image_name()
        elif item == "docker_file":
            return self.get_docker_file()
        elif item == "version":
            return self.get_version()
        elif item == "command":
            return self.get_command()
        elif item == "action":
            return self.get_action()
        elif item == "environment":
            return self.get_environment()
        elif item == "silent":
            return "Yes" if self.get_silent() == True else "No"
        else:
            return None
        
    def __setitem__(self, key, value):
        if key == "image_name":
            return self.set_image_name(value)
        elif key == "docker_file":
            return self.set_docker_file(value)
        elif key == "version":
            return self.set_version(value)
        elif key == "command":
            return self.set_command(value)
        elif key == "action":
            return self.set_action(value)
        elif key == "environment":
            return self.set_environment(value)
        elif key == "silent":
            return self.set_silent(value)
        else:
            return None
        
    def __str__(self):
        return "image_name: {}, docker_file: {}, version: {}, command: {}, action: {}, environment: {}"\
            .format(
                self.get_image_name(),
                self.get_docker_file(),
                self.get_version(),
                self.get_command(),
                self.get_action(),
                self.get_environment(),
            )
