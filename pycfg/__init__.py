'''
Python module which parses and handle configurations as TOML format.
'''

# ref: https://packaging.python.org/tutorials/packaging-projects/

__name__ = 'pycfg'
__version__ = '0.1.0'
_spec_ = '0.5.0'

from pycfg import config

load_config = config.load_config
