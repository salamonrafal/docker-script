from app.Validators.GroupValidator import GroupValidator
from app.Models import Parameters
from app.Exceptions.ValidationException import ValidationException
from app.Constants import *

class DockerComposeCommandGroupValidator(GroupValidator):
    @staticmethod
    def validate(*args):
        (parameters,) = args
        if isinstance(parameters, Parameters):
            
            pass
