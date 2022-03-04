from app.Interfaces import ValidatorInterface
from app.Models.Parameters import Parameters
from app.Validators.DockerContainerCommandGroupValidator import DockerContainerCommandGroupValidator
from app.Validators.DockerImageCommandGroupValidator import DockerImageCommandGroupValidator
from app.Validators.DockerComposeCommandGroupValidator import DockerComposeCommandGroupValidator
from app.Validators.BuildCommandGroupValidator import BuildCommandGroupValidator
from app.Validators.CleanCommandGroupValidator import CleanCommandGroupValidator
from app.Exceptions import ValidationException


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
