import os
import sys
import logging
from utils import Singleton

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
logger.debug({'default_encoding': sys.getdefaultencoding()})

f = logging.Formatter('[L:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', datefmt='%d-%m-%Y %H:%M:%S')

class Config:
    __metaclass__ = Singleton

    host = os.getenv('HOST', '127.0.0.1')
    port = os.getenv('PORT', '9999')


def make_config():
    return Config()


config = make_config()
