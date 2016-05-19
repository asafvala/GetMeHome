from django.core.management.base import BaseCommand

import time
import settings
import consts


class UpdateDB(BaseCommand):

    def handle(self, *args, **options):
        def add_trip(tid, trips):
            if tid in trips: return
            trips[tid]  = Trip(tid)

        def parse_line(line, trips):
            tid = line.split(",")[0]
            add_trip(tid, trips)
            trips[tid].add_stop(line)

        all_trips = {}

        start = time.clock()

        with open(settings.BUS_DATA_DIR+"/"+consts.STOP_TIME_FILE_NAME,'r') as f:
            for line in f.readlines()[1:]:
                print line
                #parse_line(line,all_trips)

        ttl  = time.clock() - start
        print time.strftime( '%H:%M:%S', time.gmtime(ttl) )
