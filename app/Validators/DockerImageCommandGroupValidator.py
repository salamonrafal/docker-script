from app.Validators.GroupValidator import GroupValidator
from app.Models import Parameters


class DockerImageCommandGroupValidator(GroupValidator):
    @staticmethod
    def validate(*args):
        (parameters,) = args
        if isinstance(parameters, Parameters):
            pass
