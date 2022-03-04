import inspect
import re
from pprint import pprint

VALUE_SEPARATOR = ": "
COMMENT_SIGN = "# "
LIST_SEPARATOR = ","


class ShortAliases:
    __metadata: dict = {}
    __cache: dict = {}
    
    def get_shorts(self) -> dict: return self.__metadata
    
    def get_cache(self) -> dict: return self.__cache
    
    def set_shorts(self, key: str, value: str, value_type: str): self.__metadata[key] = {"long_name": value, "type": value_type}
    
    def set_cache(self, key: str, value: []): self.__cache[key] = value
pass

def extract_lines(text, obj, return_type_value):
    lines = text.split('\n')
    line_num = 0

    for line in lines:
        obj = extract_short_names(line, line_num, obj, return_type_value)
        obj = extract_cache_data(line, line_num, obj)
    
        line_num = line_num + 1
    return obj

def extract_short_names(line, line_num, obj, return_type_value):
    if line != "" and line_num == 0:
        a = line.strip(). \
            replace(COMMENT_SIGN, ""). \
            split(VALUE_SEPARATOR)
        
        obj.set_shorts(obj, a[1], a[0], return_type_value)
    return obj

def extract_cache_data(line, line_num, obj):
    pre_text = "cache "
    pattern = r"(^" + COMMENT_SIGN + pre_text + ")(.*)"

    if line != "" and \
        line_num == 1 and \
        re.match(pattern,  line):
        
        a = line.strip(). \
            replace(COMMENT_SIGN, "").\
            replace(pre_text, "").\
            split(VALUE_SEPARATOR)
        
        list_cache_fields = a[1].split(LIST_SEPARATOR)
        obj.set_cache(obj, a[0], list_cache_fields)
    return obj

def param_shorts(obj: ShortAliases) -> ShortAliases:
    members = inspect.getmembers(obj)
    
    for member in members:
        k, v = member
        
        
        if hasattr(v, '__call__'):
            c = inspect.getcomments(v)
            if c is not None:
                return_type_value: str = str
                
                try:
                    sig = inspect.signature(v)
                    return_type_value = eval(sig.return_annotation.__name__)
                except ValueError:
                    pass
                
                if hasattr(c, "find"):
                    obj = extract_lines(c, obj, return_type_value)
    
    return obj

    
    
