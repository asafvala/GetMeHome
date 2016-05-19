from django.core.management.base import BaseCommand

import time
import settings
import consts
import pandas

from parser.objects import *

class Parser:
    def __init__(self, trips_file, stops_file, routes_file = None):
        self._trips = {}
        self._stops = {}
        self._routes = {}
        self._init_all_trips(trips_file)
        self._init_all_stops(stops_file)
        if routes_file:
            self._add_all_routes(routes_file)

    def _init_all_trips(self, fname):
        with open(fname, 'r') as f:
            first = True
            for line in f:
                if first: first = False; continue
                tid = line.split(",")[0]
                self._init_trip(tid)

    def _init_all_stops(self, fname):
        f = pandas.read_csv(fname)
        num_stops = len(f[consts.StopsFileHeaders.STOP_ID])

        for stop_ind in range(num_stops):
            sid = f[consts.StopsFileHeaders.STOP_ID][stop_ind]
            scode = f[consts.StopsFileHeaders.STOP_CODE][stop_ind]

            self._init_stop(sid,scode)

    def _init_all_routes(self, fname):
        f = pandas.read_csv(fname)
        num_stops = len(f[consts.STOP_ROUTE_ID_HEADER])

        for stop_ind in range(num_stops):
            # we only do bus routes for now
            if f[consts.RoutesFileHeaders.ROUTE_TYPE][stop_ind] ==
                            consts.RoutesFileHeaders.BUS_TYPE_VAL:
                rid = f[consts.RoutesFileHeaders.ROUTE_ID][stop_ind]

                # self._routes[  ]

    def _init_stop(self, sid, scode):
        if sid in self._trips: return
        self._stops[sid] = Stop(sid, scode)

    def _init_trip(self, tid):
        if tid in self._trips: return
        self._trips[tid] = Trip(tid)

    def parse_trip_line(self, line):
        tid = line.split(",")[0]

        # This will add a trip if needed
        self._trips[tid].add_stop(line)


class UpdateDB(BaseCommand):

    def handle(self, *args, **options):
        start = time.clock()
        trips_fname = settings.BUS_DATA_DIR+"/"+consts.FileNames.STOP_TIME_FILE_NAME
        stops_fname = settings.BUS_DATA_DIR+"/"+consts.FileNames.STOPS_FILE_NAME)

        parser_obj = Parser(trips_fname,stops_fname)
        with open(trips_fname,'r') as f:
            for line in f.readlines()[1:]:
                # print line
                Parser.parse_trip_line(line)

        ttl  = time.clock() - start
        print time.strftime( '%H:%M:%S', time.gmtime(ttl) )
