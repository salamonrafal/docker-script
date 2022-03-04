import inspect


VALUE_SEPARATOR = ": "
COMMENT_SIGN = "# "


class ShortAliases:
    __metadata: dict = {}
    
    def get_shorts(self) -> dict: return self.__metadata
    
    def set_shorts(self, key: str, value: str): self.__metadata[key] = value


def param_shorts(obj: ShortAliases) -> ShortAliases:
    members = inspect.getmembers(obj)
    
    for member in members:
        k, v = member
        if hasattr(v, '__call__'):
            c = inspect.getcomments(v)
            if c is not None:
                a = c.strip(). \
                    replace(COMMENT_SIGN, ""). \
                    split(VALUE_SEPARATOR)
                
                obj.set_shorts(obj, a[1], a[0])
    
    return obj
