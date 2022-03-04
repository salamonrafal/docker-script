from app.Interfaces import WriterInterface
import yaml


class YamlWriter(WriterInterface):
    def write(self, name: str, data: dict) -> bool:
        with open(name, 'w') as file:
            documents = yaml.dump(data, file)
            pass
        return True
