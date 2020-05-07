# coding=utf-8
# --- 00 # <editor-fold desc="system">

# </editor-fold>

# --- 02 # <editor-fold desc="myself">

# </editor-fold>

class Demo(object):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self._error0 = None

    @property
    def error0(self):
        return self._error0


