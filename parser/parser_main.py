from django.core.management.base import BaseCommand

import time
import settings
import consts
import pandas

from parser.objects.stop import Stop, StopsParser
from parser.objects.trip import Trip, TripsParser
from parser.objects.agency import Agency, AgencyParser
from parser.objects.calendar import Service, SerivcesParser

class Parser:
    def __init__(self):
        self._trips_parser = TripsParser()
        self._stops_parser = StopsParser()
        self._agencies_parser = AgencyParser()
        self._services_parser = SerivcesParser()

    def parse(self):
        # Parse trips first
        with open(consts.FileNames.get_trips_name(),'r') as f:
            next(f)
            for line in f:
                self._parse_trip_line(line)

    def init(self):
        routes_file = None

        # self._trips_parser.parse( consts.FileNames.get_trips_name() )
        self._stops_parser.parse( consts.FileNames.get_stops_name() )
        self._agencies_parser.parse( consts.FileNames.get_agencies_name() )
        self._services_parser.parse( consts.FileNames.get_calendar_name() )

        self._trips = self._trips_parser.get()
        self._stops = self._stops_parser.get()
        self._agencies = self._agencies_parser.get()
        self._services = self._services_parser.get()
        print self._agencies
        if routes_file:
            self._add_all_routes(routes_file)

    # def _init_all_routes(self, fname):
    #     f = pandas.read_csv(fname)
    #     num_stops = len(f[consts.STOP_ROUTE_ID_HEADER])
    #
    #     for stop_ind in range(num_stops):
    #         # we only do bus routes for now
    #         if f[consts.RoutesFileHeaders.ROUTE_TYPE][stop_ind] == \
    #                         consts.RoutesFileHeaders.BUS_TYPE_VAL:
    #             rid = f[consts.RoutesFileHeaders.ROUTE_ID][stop_ind]
    #
    #             # self._routes[  ]

    def _parse_trip_line(self, line):
        tid = line.split(",")[0]

        if tid not in self._trips:
            raise ValueError("Trip id [%s] not found in trips"%tid)

        # This will add a trip if needed
        self._trips[tid].add_stop(line)


class UpdateDB(BaseCommand):

    def handle(self, *args, **options):
        start = time.clock()

        parser_obj = Parser()
        parser_obj.init()
        parser_obj.parse()

        ttl  = time.clock() - start
        print time.strftime( '%H:%M:%S', time.gmtime(ttl) )
