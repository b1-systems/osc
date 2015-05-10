#!/usr/bin/env python

# this wrapper exists so it can be put into /usr/bin, but still allows the
# python module to be called within the source directory during development

import locale
import sys
import os

from osc import commandline, babysitter

try:
# this is a hack to make osc work as expected with utf-8 characters,
# no matter how site.py is set...
    reload(sys)
    loc = locale.getpreferredencoding()
    if not loc:
        loc = sys.getpreferredencoding()
    sys.setdefaultencoding(loc)
    del sys.setdefaultencoding
except NameError:
    #reload, neither setdefaultencoding are in python3
    pass

# avoid buffering output on pipes (bnc#930137)
if sys.stdout.name == '<stdout>':
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

osccli = commandline.Osc()

r = babysitter.run(osccli)
sys.exit(r)
