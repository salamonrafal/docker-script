from app.Validators.GroupValidator import GroupValidator
from app.Models import Parameters
from app.Exceptions.ValidationException import ValidationException
from app.Constants import *

class DockerContainerCommandGroupValidator(GroupValidator):
    @staticmethod
    def validate(*args):
        (parameters,) = args
        if isinstance(parameters, Parameters):
            action = parameters.get_action()
    
            if action == "":
                raise ValidationException("Field {} should not be empty".format("action"))
            
            if action not in LIST_DOCKER_CONTAINER_ACTIONS:
                raise ValidationException("Field {} should not have correct value. Should be: {}".format("action", LIST_DOCKER_CONTAINER_ACTIONS))
            
            pass
