from app.Models import CommandParamsCollection, CommandParam
from app.Exceptions import WrongNumberParametersException


class BuilderCommandParams:

    # [['f', 'ddd'], ['fix'], ['-not_alias', 'with'], ['-not_alias_flg]]
    @staticmethod
    def build_from_list(list_params: list) -> CommandParamsCollection:
        """
        :rtype: CommandParamsCollection
        """

        collection = CommandParamsCollection()

        for param_item in list_params:
            if isinstance(param_item, list):
                command_param = BuilderCommandParams._create_command_params_from_list(param_item)
                collection.__add__(command_param)
            if isinstance(param_item, str):
                command_param = BuilderCommandParams._create_command_param_value_text(param_item)
                collection.__add__(command_param)

        return collection

    @staticmethod
    def _create_command_param_value_text(param_item: str) -> CommandParam:
        return CommandParam(param_item, None, False, True)

    @staticmethod
    def _create_command_params_from_list(param_item: list) -> CommandParam:
        if len(param_item) == 1:
            key_clean_name = BuilderCommandParams._clean_key_name(param_item[0])

            return CommandParam(key_clean_name, None, BuilderCommandParams._check_is_alias_for_list(param_item[0]))
        elif len(param_item) == 2:
            key_clean_name = BuilderCommandParams._clean_key_name(param_item[0])

            return CommandParam(
                key_clean_name,
                param_item[1],
                BuilderCommandParams._check_is_alias_for_list(param_item[0])
            )
        else:
            raise WrongNumberParametersException("Wrong number of command params: {}".format(len(param_item)))

    # {'f' = 'value', 'f' = None, '-not_alias' = 'value', '-not_alias_flag' = None}
    @staticmethod
    def build_from_dict(struct_params: dict) -> CommandParamsCollection:
        """
        :rtype: CommandParamsCollection
        """

        collection = CommandParamsCollection()

        for key in struct_params:
            value = struct_params[key]
            key_clean_name = BuilderCommandParams._clean_key_name(key)
            is_alias = BuilderCommandParams._check_is_alias_for_dict(key)
            is_text_value = BuilderCommandParams._check_is_text_value(key)

            key_clean_name, value, = BuilderCommandParams._transform_text_value_from_value(
                is_text_value,
                value,
                key_clean_name
            )

            command_param = CommandParam(
                key_clean_name,
                value,
                is_alias,
                is_text_value
            )

            collection.__add__(command_param)

        return collection

    @staticmethod
    def _transform_text_value_from_value(is_text_value: bool, value: str, key_clean_name: str) -> tuple:

        if is_text_value and value is not None:
            key_clean_name = value
            value = None

        return key_clean_name, value,

    @staticmethod
    def _check_is_text_value(key_name: str) -> bool:
        if "--" in key_name or "-" in key_name:
            return False
        else:
            return True

    @staticmethod
    def _check_is_alias_for_dict(key_name: str) -> bool:
        """

        :param key_name:
        :return:  bool
        """
        if "--" in key_name:
            return False
        elif "-" in key_name:
            return True
        else:
            return True

    @staticmethod
    def _check_is_alias_for_list(key_name: str) -> bool:
        """

        :param key_name:
        :return: bool
        """
        if "-" in key_name:
            return False
        else:
            return True

    @staticmethod
    def _clean_key_name(key_name: str) -> str:
        """

        :param key_name:
        :return: str
        """
        key_name = key_name.replace("--", "")
        key_name = key_name.replace("-", "")

        return key_name
    pass
