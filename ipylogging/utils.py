# vim: expandtab tabstop=4 shiftwidth=4

import sys

from logging import Formatter

if sys.version_info.major == 3:
    from html import escape
elif sys.version_info.major == 2:
    from cgi import escape
else:
    raise Exception('Invalid version of Python')

def _html_escape(s):
    return escape(s, quote=True)

def _in_ipython():
    try:
        from IPython import get_ipython

        if get_ipython() is not None:
            return True

        return False

    except ImportError:
        return False

    return False

def _make_formatter(show_time, show_name, show_level):
    parts = []

    if show_time:
        parts.append('%(asctime)s')

    if show_name:
        parts.append('%(name)s')

    if show_level:
        parts.append('%(levelname)s')

    parts.append('%(message)s')

    return Formatter(' '.join(parts))
