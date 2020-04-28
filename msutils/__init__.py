from .util import *
from .dateutil import *
from .mathutil import *
from .osutil import *
from .pathutil import *
from .rangeutil import *
from .jsonmap import *
from .clonable import *
from .jsonutil import *
from .klass import *
from .httputil import *
from .uuidutil import *
from .xmlutil import *
from pathlib import Path

__all__ = (
    util.__all__ 
    + dateutil.__all__ 
    + mathutil.__all__ 
    + osutil.__all__ 
    + pathutil.__all__ 
    + rangeutil.__all__ 
    + jsonmap.__all__ 
    + clonable.__all__ 
    + jsonutil.__all__ 
    + klass.__all__
    + httputil.__all__
    + uuidutil.__all__
    + xmlutil.__all__
)

version_filename = "VERSION"

curr_path = Path(__file__)
curr_dir = curr_path.parent
version_path = curr_dir / version_filename

with open(str(version_path)) as f:
	__version__ = f.read()
