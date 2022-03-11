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
            if len(param_item) == 1:
                key_clean_name = BuilderCommandParams._clean_key_name(param_item[0])
                command_param = CommandParam(key_clean_name, None, BuilderCommandParams._check_is_alias(param_item[0]))
            elif len(param_item) == 2:
                key_clean_name = BuilderCommandParams._clean_key_name(param_item[0])
                command_param = CommandParam(
                    key_clean_name,
                    param_item[1],
                    BuilderCommandParams._check_is_alias(param_item[0])
                )
            else:
                raise WrongNumberParametersException("Wrong number of command params: {}".format(len(param_item)))

            collection.__add__(command_param)

        return collection

    # {'f' = 'value', 'f' = None, '-not_alias' = 'value', '-not_alias_flag' = None}
    @staticmethod
    def build_from_struct(struct_params: dict) -> CommandParamsCollection:
        """
        :rtype: CommandParamsCollection
        """

        collection = CommandParamsCollection()

        for key in struct_params:
            value = struct_params[key]
            key_clean_name = BuilderCommandParams._clean_key_name(key)
            is_alias = BuilderCommandParams._check_is_alias(key)

            command_param = CommandParam(
                key_clean_name,
                value,
                is_alias
            )

            collection.__add__(command_param)

        return collection

    @staticmethod
    def _check_is_alias(key_name: str) -> bool:
        """

        param key_name:
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
        return key_name.replace("-", "")
    pass
