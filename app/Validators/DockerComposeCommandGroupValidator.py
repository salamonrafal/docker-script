from app.Validators.GroupValidator import GroupValidator
from app.Models import Parameters


class DockerComposeCommandGroupValidator(GroupValidator):
    @staticmethod
    def validate(*args):
        (parameters,) = args
        if isinstance(parameters, Parameters):
            
            pass
