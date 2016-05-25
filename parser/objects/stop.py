import pandas
from parser import consts

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

class StopsParser:
    def __init__(self):
        self._stops = {}

    def _init_all_stops(self, fname):
        f = pandas.read_csv(fname)
        num_stops = len(f[consts.StopsFileHeaders.STOP_ID])

        for stop_ind in range(num_stops):
            sid = f[consts.StopsFileHeaders.STOP_ID][stop_ind]
            scode = f[consts.StopsFileHeaders.STOP_CODE][stop_ind]

            self._init_stop(sid,scode)

    def _init_stop(self, sid, scode):
        if sid in self._stops: return
        self._stops[sid] = Stop(sid, scode)

    def parse(self, stops_file):
        self._init_all_stops(stops_file)

    def get(self):
        return self._stops
