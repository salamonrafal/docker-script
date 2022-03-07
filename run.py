import sys
from app import Bootstrap, UnhandledCommandException
from app.Di.Registers import Sdi

app = Bootstrap(Sdi)
try:
    app.bootstrap(sys.argv)
except UnhandledCommandException as ex:
    app.error(ex)
    pass
