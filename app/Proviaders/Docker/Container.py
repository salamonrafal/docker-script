from app.Interfaces import ProviderInterface
from typing import List
from app.Interfaces import ProviderInterface
from app.Models import Command, ImageName

class Container(ProviderInterface):
    __APPLICATION = "docker"
    __COMMAND_NAME = "container"
    
    def execute(self, *args):
        (parameters,) = args
        image_name = ImageName(parameters.get_image_name(), parameters.get_version())
        params: List = [
            ["t", image_name],
            ["f", parameters.get_docker_file()],
            ["."]
        ]
        command = Command(self.__APPLICATION, self.__COMMAND_NAME, params)

        print("Command: ", command)
        
        if not parameters.get_silent():
            print(cmd)
            
        pass
