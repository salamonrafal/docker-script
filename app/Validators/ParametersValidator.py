from lib.Interfaces import ValidatorInterface
from lib.Models.Parameters import Parameters
from lib.Validators.DockerContainerCommandGroupValidator import DockerContainerCommandGroupValidator
from lib.Validators.DockerImageCommandGroupValidator import DockerImageCommandGroupValidator
from lib.Validators.DockerComposeCommandGroupValidator import DockerComposeCommandGroupValidator
from lib.Validators.BuildCommandGroupValidator import BuildCommandGroupValidator
from lib.Validators.CleanCommandGroupValidator import CleanCommandGroupValidator
from lib.Exceptions import ValidationException


class ParametersValidator(ValidatorInterface):
    parameters: Parameters = Parameters()
    
    def __init__(self, parameters: Parameters):
        self.parameters = parameters
        pass
    
    def validate(self):
        command = self.parameters.get_command()

        if command is None or command == "":
            raise ValidationException("command is required. It cannot be empty")

        match command:
            case "build":
                BuildCommandGroupValidator.validate(self.parameters)
                pass

            case "docker-image":
                DockerImageCommandGroupValidator.validate(self.parameters)
                pass

            case "docker-compose":
                DockerComposeCommandGroupValidator.validate(self.parameters)
                pass

            case "docker-container":
                DockerContainerCommandGroupValidator.validate(self.parameters)
                pass

            case "clean":
                CleanCommandGroupValidator.validate(self.parameters)
                pass
        pass
