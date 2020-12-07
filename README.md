# ipylogging

Easy logging in Jupyter notebooks.

Most people will be fine with the default options from `get_logger()`.

```python
import ipylogging

logger = ipylogging.get_logger()
...
logger.debug('The nitty gritty.')
logger.info('Nice to know.')
logger.warning('It could be worse.')
logger.error("It's worse.")
logger.critical('Houston, we have a problem.')
```

`get_logger()` also takes the following options:
- `name` - The name of the logger passed to `logging.getLogger()`.  Defaults to `ipylogging`.
- `show_time` - Whether to show the time.  Defaults to `True`.
- `show_name` - Whether to show the logger name.  Defaults to `False`.
- `show_level` - Whether to show the log level (eg. `INFO`, `ERROR`, etc.).  Defaults to `True`.

If you want even more control, you can also use `IPythonHandler` directly, which is a standard `logging.Handler` that supports all the same stuff as `logging.StreamHandler`.

```python
import logging
import ipylogging
logger = logging.getLogger('foo')
handler = ipylogging.IPythonHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.ERROR)
```

ipylogging also works outside of Jupyter, in which case `get_logger()` will simply return a normal Python logging.Logger with a StreamHandler.  This is useful when writing modules that might be used inside or outside of notebooks.
