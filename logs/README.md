Use the debug.log file instead of printing to console:

```
from logging import getLogger
from django.conf import settings

log = getLogger(settings.DEBUG_LOGGER)

log.debug('my debug info')
```
