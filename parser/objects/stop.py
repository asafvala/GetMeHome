
class Stop:
    def __init__(self, sid):
        self._sid = sid
        self._lines_using = set()
        self._routes_using = set()
