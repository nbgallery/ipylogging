# vim: expandtab tabstop=4 shiftwidth=4

import logging

from .utils import _html_escape

try:
    from IPython.display import display, HTML
except ImportError:
    pass

def _ipython_html(msg, bgcolor, fgcolor='black'):
    msg = _html_escape(msg)
    style = 'font-family:monospace;background:{bgcolor};color:{fgcolor}'.format(bgcolor=bgcolor, fgcolor=fgcolor)
    htm = '<div style="{style}"><pre>{msg}</pre></div>'.format(style=style, msg=msg)
    display(HTML(htm))

def _log_color(level):
    color_map = {
        logging.DEBUG:    '#eee',
        logging.INFO:     '#e6fee6',
        logging.WARNING:  'lightyellow',
        logging.ERROR:    'lightpink',
        logging.CRITICAL: 'red',
    }

    return color_map.get(level, 'plum')

class IPythonHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            message = self.format(record)
            _ipython_html(message, _log_color(record.levelno))
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
