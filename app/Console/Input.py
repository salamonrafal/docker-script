from app.Locale import Labels


class Input:
    @staticmethod
    def input(label: Labels, key: str, lang:str = "en_en", path :str = ""):
        print(label.get_label(lang, key, path))
        return input()
