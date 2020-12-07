# vim: expandtab tabstop=4 shiftwidth=4

import logging

from .utils import _in_ipython

if _in_ipython():
    from .logger import IPythonHandler

def get_simple_logger():
    logger = logging.getLogger('ipylogging')

    if _in_ipython():
        handler = IPythonHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    else:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
