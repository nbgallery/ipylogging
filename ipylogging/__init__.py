# vim: expandtab tabstop=4 shiftwidth=4

import logging

from .utils import _in_ipython, _make_formatter

if _in_ipython():
    from .handler import IPythonHandler

def get_logger(name='ipylogging', show_time=True, show_name=False, show_level=True):
    logger = logging.getLogger(name)
    formatter = _make_formatter(show_time, show_name, show_level)

    if _in_ipython():
        handler = IPythonHandler()
    else:
        handler = logging.StreamHandler()

    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
