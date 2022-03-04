from app.Models.Yaml import Docker, YamlObject
from app.Interfaces import ReaderInterface, WriterInterface, ProviderInterface
from app.Constants import CONFIG_CACHE_PARAMETERS_FILE_PATH, DEFAULT_LANGUAGE
from app.Console import Print, Input
from app.Locale.Labels import Labels

CMD_CONFIRMATION_SIGN = "Y"


class Init(ProviderInterface):
    yaml_reader: ReaderInterface
    yaml_writer: WriterInterface
    labels: Labels
    label_path = "providers.init"

    def __init__(self, provider_type_arg: str, yaml_reader: ReaderInterface, yaml_writer: WriterInterface,
                 labels: Labels):
        super().__init__(provider_type_arg)
        self.yaml_reader = yaml_reader
        self.yaml_writer = yaml_writer
        self.labels = labels
        pass

    def execute(self, *args) -> bool:
        Print.label(self.labels, "headline", DEFAULT_LANGUAGE, self.label_path)
        inputs = self.__handle_inputs()
        self.__print_confirmation(*inputs)
        confirmed = Input.input(self.labels, "save_confirmation", DEFAULT_LANGUAGE, self.label_path)
        docker_model = self.__get_docker_data_settings(*inputs)

        if CMD_CONFIRMATION_SIGN == str(confirmed).upper():
            Print.label(self.labels, "confirm_is_caved", DEFAULT_LANGUAGE, self.label_path)
            self.__save_setting_data(docker_model)
        else:
            Print.label(self.labels, "confirm_is_aborted", DEFAULT_LANGUAGE, self.label_path)

        return True

    def __save_setting_data(self, docker_model: YamlObject):
        data: dict = {"docker": docker_model.to_dict()}
        self.yaml_writer.write(CONFIG_CACHE_PARAMETERS_FILE_PATH, data)

        pass

    @staticmethod
    def __get_docker_data_settings(*args) -> YamlObject:
        (
            docker_file_input,
            environment_input,
            image_name_input,
            version_input,
            prefix_name_input,
            containers_name_input,
        ) = args

        return Docker(
            docker_file_input,
            environment_input,
            image_name_input,
            version_input,
            prefix_name_input,
            containers_name_input
        )

    def __handle_inputs(self):
        docker_file_input = Input.input(self.labels, "docker_file_input", DEFAULT_LANGUAGE, self.label_path)
        environment_input = Input.input(self.labels, "environment_input", DEFAULT_LANGUAGE, self.label_path)
        image_name_input = Input.input(self.labels, "image_name_input", DEFAULT_LANGUAGE, self.label_path)
        version_input = Input.input(self.labels, "version_input", DEFAULT_LANGUAGE, self.label_path)
        prefix_name_input = Input.input(self.labels, "prefix_name_input", DEFAULT_LANGUAGE, self.label_path)
        containers_name_input = Input.input(self.labels, "containers_name_input", DEFAULT_LANGUAGE, self.label_path)
        print()

        return docker_file_input, \
               environment_input, \
               image_name_input, \
               version_input, \
               prefix_name_input, \
               containers_name_input,

    def __print_confirmation(self, *args):
        (
            docker_file_input,
            environment_input,
            image_name_input,
            version_input,
            prefix_name_input,
            containers_name_input,
        ) = args

        Print.label(self.labels, "caption_confirmation", DEFAULT_LANGUAGE, self.label_path)
        Print.label(self.labels, "docker_file_confirm", DEFAULT_LANGUAGE, self.label_path, docker_file_input)
        Print.label(self.labels, "environment_confirm", DEFAULT_LANGUAGE, self.label_path, environment_input)
        Print.label(self.labels, "image_name_confirm", DEFAULT_LANGUAGE, self.label_path, image_name_input)
        Print.label(self.labels, "version_confirm", DEFAULT_LANGUAGE, self.label_path, version_input)
        Print.label(self.labels, "prefix_name_confirm", DEFAULT_LANGUAGE, self.label_path, prefix_name_input)
        Print.label(self.labels, "containers_name_confirm", DEFAULT_LANGUAGE, self.label_path, containers_name_input)
        print()

        pass
