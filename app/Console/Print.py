from app.Locale import Labels


class Print:
    @staticmethod
    def label(label: Labels, key: str, lang: str = "en_en", path: str = "", *args):
        print(label.get_label(lang, key, path).format(*args))
        pass
