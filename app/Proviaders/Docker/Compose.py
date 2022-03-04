from subprocess import run
from typing import List
from app.Interfaces import ProviderInterface
from app.Models import Command, ImageName


class Compose(ProviderInterface):
    __APPLICATION = "docker-compose"
    __COMMAND_NAME = "up"
    
    def execute(self, *args):
        (parameters,) = args
        image_name = ImageName(parameters.get_image_name(), parameters.get_version())
        params: List = [
            ["-d"]
        ]
        command = Command(self.__APPLICATION, self.__COMMAND_NAME, params)
    
        print("Command: ", command)
    
        cmd = run(command.__str__()).stderr
    
        if not parameters.get_silent():
            print(cmd)
    
        pass
