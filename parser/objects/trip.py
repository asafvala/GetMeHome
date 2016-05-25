from collections import defaultdict
import datetime, time
from parser import consts

class Trip:
    def __init__(self, tid):
        self._id = tid
        self._stops = {}

    def add_stop(self, line):
        line = line.split(",")
        sid = int( line[consts.StopTimesIndeces.STOP_ID_IND] )
        seq = int ( line[consts.StopTimesIndeces.STOP_SEQUENCE_IND] )
        val = (sid, line[consts.StopTimesIndeces.DEPARTURE_TIME_IND],
                    line[consts.StopTimesIndeces.ARRIVAL_TIME_IND])

        self._stops[seq] = val

    def get_trip_duration(self):
        return self._get_duration(min(self._stops), max(self._stops))

    def get_all_durations(self):
        durations  = []

        keys = self._stops.keys().sort()
        for ind in range(len(keys)-1):
            durations.append(self._get_duration(keys[ind], keys[ind+1]))

        return durations

    def _get_duration(self, start_ind, end_ind):
        # start_ind = min(self._stops)
        # end_ind = max(self._stops)

        start_time = self._stops[start_ind][1]
        start_time_val = time.strptime(start_time.split(',')[0],'%H:%M:%S')
        start_time_sec = datetime.timedelta(hours=start_time_val.tm_hour,
                                            minutes=start_time_val.tm_min,
                                            seconds=start_time_val.tm_sec).total_seconds()

        end_time = self._stops[end_ind][2]
        end_time_val = time.strptime(end_time.split(',')[0],'%H:%M:%S')
        end_time_sec = datetime.timedelta(hours=end_time_val.tm_hour,
                                            minutes=end_time_val.tm_min,
                                            seconds=end_time_val.tm_sec).total_seconds()

        duration_sec = end_time_sec-start_time_sec
        return duration_sec
        # return time.strftime( '%H:%M:%S', time.gmtime(duration_sec) )


    def __str__(self):
        res  = "Trip ID: %s, #Stops= %d\n" % (self._id, len(self._stops) )
        for v in self._stops:
            res+= "%s -> %s\n"%(str(v), str(self._stops[v]))
        res += "Trip Duration: %s"%str( self.get_duration() )
        return res

class TripsParser:
    def __init__(self):
        self._trips = {}

    def _init_all_trips(self, fname):
        with open(fname, 'r') as f:
            next(f)
            for line in f:
                tid = line.split(",")[0]
                self._init_trip(tid)

    def _init_trip(self, tid):
        if tid in self._trips: return
        self._trips[tid] = Trip(tid)

    def parse(self, stops_file):
        self._init_all_trips(stops_file)

    def get(self):
        return self._trips
