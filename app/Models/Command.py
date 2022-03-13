from typing import List
from app.Models import CommandParamsCollection


class Command:
    params: CommandParamsCollection
    application: str
    command: str

    def __init__(self, application: str, command: str, params: CommandParamsCollection):
        self.application = application
        self.command = command
        self.params = params
        pass

    def __transform_data_dict(self):
        param_string = "{} {}".format(self.application, self.command)

        return param_string + str(CommandParamsCollection)

    def __str__(self):
        return self.__transform_data_dict()
