from app.Models import CommandParam


class CommandParamsCollection:
    _params: [CommandParam] = []

    def __init__(self, params=None):
        if params is None:
            params = []
        self._params = params

    def __add__(self, other: CommandParam):
        self._params.append(other)

    def __getitem__(self, item):
        return self._params[item]

    def __sizeof__(self):
        return len(self._params)

    def __str__(self):
        return " ".join(map(str, self._params))

    pass
