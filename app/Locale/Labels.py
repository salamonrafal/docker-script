class Labels:
    __locale__: dict
    
    def __init__(self, locale: dict):
        self.__locale__ = locale
        pass
    
    def get_label(self, language: str, key: str, path: str = None):
        if path is not None:
            return self.__get_locale_in_path(key, path, language)
        else:
            return self.__locale__[language][key]
        pass
    
    def __get_locale_in_path(self, key: str, path: str, language: str):
        items = path.split(".")
        current_locale = self.__locale__[language]
        
        for item in items:
            current_locale = current_locale[item]
            
        return current_locale[key]
