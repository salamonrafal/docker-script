from app.Interfaces import ProviderFactoryInterface, ReaderInterface, WriterInterface
from app import ParametersFactory
from app.Exceptions import GeneralExceptions


class Bootstrap:
    provider_factory: ProviderFactoryInterface = None
    file_reader: ReaderInterface = None
    file_writer: WriterInterface = None
    parameters_factory: ParametersFactory = None

    # ******************************************************************

    def __init__(
            self,
            provider_factory: ProviderFactoryInterface = None,
            file_reader: ReaderInterface = None,
            file_writer: WriterInterface = None,
            parameters_factory: ParametersFactory = None
    ):
        self.provider_factory = provider_factory
        self.file_reader = file_reader
        self.file_writer = file_writer
        self.parameters_factory = parameters_factory
        pass

    # ******************************************************************

    def bootstrap(self, argv):
        parameters = self.parameters_factory.prepare_parameters(argv)
        self.provider_factory.register(parameters.get_command()).execute(parameters)
        pass

    # ******************************************************************

    @staticmethod
    def error(ex: GeneralExceptions):
        print(ex)
        pass
