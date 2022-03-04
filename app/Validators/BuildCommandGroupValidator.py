from app.Models import Parameters
from app.Validators.GroupValidator import GroupValidator
from app.Exceptions.ValidationException import ValidationException
from app.Constants import *


class BuildCommandGroupValidator(GroupValidator):
    @staticmethod
    def validate(*args):
        (parameters,) = args
        
        if isinstance(parameters, Parameters):
            image_name = parameters.get_image_name()
            environment = parameters.get_environment()

            if image_name == "":
                raise ValidationException("Field {} should not be empty".format("image_name"))
            
            if environment == "":
                raise ValidationException("Field {} should not be empty".format("environment"))
            
            if environment not in LIST_ENVIRONMENTS:
                raise ValidationException("Field {} should not have correct value. Should be: {}".format("environment", LIST_ENVIRONMENTS))
            
        pass
