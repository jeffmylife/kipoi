from __future__ import absolute_import

__author__ = 'Kipoi team'
__version__ = '0.0.1'


# available modules
from . import model_handling
from . import utils
from . import variant_effects


# Setup logging
import logging

log_formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(name)s] %(message)s')
_logger = logging.getLogger('model-zoo')

_handler = logging.StreamHandler()
_handler.setLevel(logging.INFO)
_handler.setFormatter(log_formatter)
_logger.setLevel(logging.INFO)
_logger.addHandler(_handler)
