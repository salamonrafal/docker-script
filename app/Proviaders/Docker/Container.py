from typing import List
from app.Interfaces import ProviderInterface
from app.Models import Command, ImageName
from app.Di import SimplyDi
from app.Builders import BuilderCommandParams


class Container(ProviderInterface):
    __APPLICATION = "docker"
    __COMMAND_NAME = "container"

    _command_param_builder: BuilderCommandParams

    def __init__(self, provider_type_arg: str, sdi: SimplyDi):
        super().__init__(provider_type_arg, sdi)

        self._command_param_builder = sdi.get_service('command_params_builder')
        pass

    def execute(self, *args):
        (parameters,) = args
        image_name = ImageName(parameters.get_image_name(), parameters.get_version())

        command_params_collection = self._command_param_builder.build_from_list([
            ["t", image_name],
            ["f", parameters.get_docker_file()],
            ["."]
        ])

        command = Command(self.__APPLICATION, self.__COMMAND_NAME, command_params_collection)
        
        if not parameters.get_silent():
            print("Command: ", command)
            
        pass
