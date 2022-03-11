class CommandParam:
    _key: str = ""
    _value: str = None
    _is_alias: bool = False

    def __init__(self, key: str, value: str = None, is_alias: bool = False):
        self._key = key
        self._value = value
        self._is_alias = is_alias
        pass

    def get_value(self):
        return self._value

    def get_key(self):
        return self._key

    def is_alias(self):
        return self._is_alias

    def _get_command_format(self):
        if self._value is None:
            return "{}".format(self._key)
        else:
            return "{} {}".format(self._key, self._value)

    def __str__(self):
        if self.is_alias():
            return "-{}".format(self._get_command_format())
        else:
            return "--{}".format(self._get_command_format())

    pass
