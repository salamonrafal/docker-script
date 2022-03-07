from app.Interfaces import ProviderFactoryInterface, ReaderInterface, WriterInterface
from app import ParametersFactory
from app.Exceptions import GeneralExceptions
from app.Locale.Labels import Labels
from app.Di import SimplyDi


class Bootstrap:
    provider_factory: ProviderFactoryInterface = None
    file_reader: ReaderInterface = None
    file_writer: WriterInterface = None
    parameters_factory: ParametersFactory = None
    labels: Labels
    script_path: str = None
    di: SimplyDi = None

    # ******************************************************************

    def __init__(
        self,
        di: SimplyDi
    ):
        self.di = di
        self.provider_factory = di.get_service("provider_factory")
        self.file_reader = di.get_service("provider_factory")
        self.file_writer = di.get_service("file_writer")
        self.parameters_factory = di.get_service("parameters_factory")
        self.labels = di.get_service("labels")
        self.script_path = di.get_service("script_dir_name")
        pass

    # ******************************************************************

    def bootstrap(self, argv):
        parameters = self.parameters_factory.prepare_parameters(argv)
        self.provider_factory\
            .register(parameters.get_command())\
            .execute(parameters)
        pass

    # ******************************************************************

    @staticmethod
    def error(ex: GeneralExceptions):
        print(ex)
        pass
