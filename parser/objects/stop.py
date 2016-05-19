
class Stop:
    def __init__(self, sid, scode):
        self._sid = sid
        self._scode = scode
        self._lines_using = set()
        self._routes_using = set()
        self._agencies = set()

    def add_agency(self, agency_id):
        self._agencies.add(agency_id)

    def add_line_using(self, line_id):
        self._lines_using.add(line_id)

    def add_route_using(self, route_id):
        self._routes_using.add(route_id)
