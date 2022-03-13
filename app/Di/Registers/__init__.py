import os
import sys
from app import ProviderFactory, ParametersFactory
from app.Constants.Locale import Locale
from app.Locale import Labels
from app.Readers import YamlReader, FileReader
from app.Writers import YamlWriter, FileWriter
from app.Di import SimplyDi
from app.Builders import BuilderCommandParams

Sdi = SimplyDi()
labels = Labels(Locale)
script_dir_name = os.path.abspath(os.path.dirname(sys.argv[0]))

# Register Variables
Sdi.registry_service('labels', labels)
Sdi.registry_service('script_dir_name', script_dir_name)

# Register Services
Sdi.registry_service('yaml_reader', YamlReader())
Sdi.registry_service('yaml_writer', YamlWriter())
Sdi.registry_service('file_reader', FileReader())
Sdi.registry_service('file_writer', FileWriter())
Sdi.registry_service('command_params_builder', BuilderCommandParams())

# Register Factories
Sdi.registry_service('provider_factory', ProviderFactory(Sdi))
Sdi.registry_service('parameters_factory', ParametersFactory(Sdi))
