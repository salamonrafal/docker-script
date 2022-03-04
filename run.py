import sys
from app import Bootstrap,\
    ProviderFactory,\
    FileWriter,\
    FileReader,\
    ParametersFactory,\
    UnhandledCommandException


app = Bootstrap(ProviderFactory(), FileReader(), FileWriter(), ParametersFactory())

# noinspection PyBroadException
try:
    app.bootstrap(sys.argv)
except UnhandledCommandException as ex:
    app.error(ex)
    pass
