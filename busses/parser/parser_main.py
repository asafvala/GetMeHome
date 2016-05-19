from django.core.management.base import BaseCommand

import time
import settings
import consts

from parser.objects import *

class Parser:
    def __init__(self):
        self._trips = {}
        self._stops = {}

    def add_trip(self, tid):
        if tid in self._trips: return
        self._trips[tid] = Trip(tid)

    def parse_trip_line(self, line):
        tid = line.split(",")[0]

        # This will add a trip if needed
        self.add_trip(tid)
        self._trips[tid].add_stop(line)


class UpdateDB(BaseCommand):

    def handle(self, *args, **options):
        start = time.clock()
        parser_obj = Parser()
        with open(settings.BUS_DATA_DIR+"/"+consts.STOP_TIME_FILE_NAME,'r') as f:
            for line in f.readlines()[1:]:
                # print line
                Parser.parse_trip_line(line)

        ttl  = time.clock() - start
        print time.strftime( '%H:%M:%S', time.gmtime(ttl) )
