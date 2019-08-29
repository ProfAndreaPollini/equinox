
from .window import equinox_create_window,equinox_run
from .utils import Borg, Observer
from .events import equinoxEvents

from pyglet.window import key
# Set default logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler



logging.getLogger(__name__).addHandler(NullHandler())

