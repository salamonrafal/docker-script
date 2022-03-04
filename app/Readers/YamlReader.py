import yaml
from app.Interfaces import ReaderInterface


class YamlReader(ReaderInterface):
    def read(self, name):
        with open(name) as file:
            documents = yaml.full_load(file)
        return documents
