from lib.Interfaces import ParametersFactoryInterface
from lib.Models import Parameters
from lib.Locale import *
from lib.Validators.ParametersValidator import ParametersValidator
import argparse


class ParametersFactory(ParametersFactoryInterface):
    def prepare_parameters(self, argv) -> Parameters:
        args = self.__parse_parameters(Parameters().get_shorts())
        parameters_updated = self.__update_parameters(Parameters(), args)
        self.__validate_parameters(parameters_updated)
        
        return parameters_updated

    # ******************************************************************

    @staticmethod
    def __validate_parameters(parameters: Parameters) -> bool:
        validator = ParametersValidator(parameters)
        return validator.validate()

    # ******************************************************************
    
    @staticmethod
    def __parse_parameters(available_parameters: dict):
        arg_parser = argparse.ArgumentParser()
    
        for short_parameter in available_parameters:
            long_parameter = available_parameters[short_parameter]
            arg_parser.add_argument(
                "-" + short_parameter,
                "--" + long_parameter,
                type=str,
                default="",
                help=locale["en_en"]["help"][long_parameter]
            )
            
        return arg_parser.parse_args()

    # ******************************************************************
    
    @staticmethod
    def __update_parameters(parameters: Parameters, args) -> Parameters:
        params = {}
        available_parameters = parameters.get_shorts()
        
        for short_parameter in available_parameters:
            long_parameter = available_parameters[short_parameter]
            
            if long_parameter in args:
                params[long_parameter] = eval("args." + long_parameter)
            else:
                params[long_parameter] = ""
        
        return Parameters(params["command"], params["image_name"], params["docker_file"], params["version"])
