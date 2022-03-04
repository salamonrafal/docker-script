from typing import List


class Command:
    params: List
    application: str
    command: str

    def __init__(self, application: str, command: str, params: List):
        self.application = application
        self.command = command
        self.params = params
        pass

    def __transform_data_dict(self):
        param_string = "{} {}".format(self.application, self.command)

        for param_data in self.params:
            current_param_string = ""
            if len(param_data) == 2:
                current_param_string = " -{} {}".format(param_data[0], param_data[1])
            elif len(param_data) == 1:
                current_param_string = " {}".format(param_data[0])

            param_string = param_string + current_param_string

        return param_string

    def __str__(self):
        return self.__transform_data_dict()
