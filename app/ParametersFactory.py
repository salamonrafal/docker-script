from typing import List
import argparse
from app.Interfaces import ParametersFactoryInterface, ReaderInterface, WriterInterface
from app.Models import Parameters
from app.Locale import Labels
from app.Validators.ParametersValidator import ParametersValidator
from app.Constants import CONFIG_CACHE_PARAMETERS_FILE_PATH, DEFAULT_LANGUAGE


class ParametersFactory(ParametersFactoryInterface):
    file_reader: ReaderInterface
    file_writer: WriterInterface
    labels: Labels
    label_path = "help"
    
    # ******************************************************************
    
    def __init__(self, file_reader: ReaderInterface, file_writer: WriterInterface, labels: Labels):
        self.file_writer = file_writer
        self.file_reader = file_reader
        self.labels = labels
        
        pass

    # ******************************************************************
    
    def prepare_parameters(self, argv) -> Parameters:
        args = self.__parse_parameters(Parameters().get_shorts())
        parameters = self.__update_parameters(Parameters(), args)
        self.__validate_parameters(parameters)
        
        return parameters

    # ******************************************************************
    
    def __handle_cache_parameters(self, parameters: Parameters) -> Parameters:
        
        if parameters.get_command() in parameters.get_cache():
            fields = parameters.get_cache()[parameters.get_command()]
            self.__save_cache_parameters(parameters, fields)
        else:
            self.__read_cache_parameters(parameters)
        
        return parameters

    # ******************************************************************
    
    def __save_cache_parameters(self, parameters: Parameters, fields: List):
        data: dict = { "docker": {} }
        
        for field in fields:
            data["docker"][field] = parameters[field]
            
        self.file_writer.write(CONFIG_CACHE_PARAMETERS_FILE_PATH, data)
        pass

    # ******************************************************************
    
    def __read_cache_parameters(self, parameters: Parameters):
        doc = self.file_reader.read(CONFIG_CACHE_PARAMETERS_FILE_PATH)
        for key in doc["docker"]:
            parameters[key] = doc["docker"][key]
        pass

    # ******************************************************************
    
    @staticmethod
    def __validate_parameters(parameters: Parameters):
        validator = ParametersValidator(parameters)
        validator.validate()
        pass

    # ******************************************************************
    
    def __parse_parameters(self, available_parameters: dict):
        arg_parser = argparse.ArgumentParser()
    
        for short_parameter in available_parameters:
            param_attr = available_parameters[short_parameter]
            arg_parser.add_argument(
                "-" + short_parameter,
                "--" + param_attr["long_name"],
                type=param_attr["type"],
                default="",
                help=self.labels.get_label(DEFAULT_LANGUAGE, param_attr["long_name"], self.label_path)
            )
            
        return arg_parser.parse_args()

    # ******************************************************************
    
    def __update_parameters(self, parameters: Parameters, args: object) -> Parameters:
        available_parameters = parameters.get_shorts()
        parameters = self.__handle_cache_parameters(parameters)
        for short_parameter in available_parameters:
            param_attr = available_parameters[short_parameter]
            if param_attr["long_name"] in args:
                value = eval("args." + param_attr["long_name"])
                
                if value != "":
                    parameters[param_attr["long_name"]] = self.__set_by_value_type(param_attr["type"], value)
        
        return parameters

    # ******************************************************************
    
    @staticmethod
    def __set_by_value_type(v_type, value):
        if v_type is bool:
            return value
        else:
            return value
