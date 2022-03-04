import sys
from app.Writers import *
from app.Readers import *
from app.Constants.Locale import Locale
from app.Locale import Labels
from app import Bootstrap,\
    ProviderFactory,\
    ParametersFactory,\
    UnhandledCommandException


labels = Labels(Locale)
app = Bootstrap(
    ProviderFactory(YamlReader(), YamlWriter(), labels),
    FileReader(),
    FileWriter(),
    ParametersFactory(YamlReader(), YamlWriter(), labels),
    labels
)

# noinspection PyBroadException
try:
    app.bootstrap(sys.argv)
except UnhandledCommandException as ex:
    app.error(ex)
    pass
