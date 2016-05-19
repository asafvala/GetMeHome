from collections import defaultdict
import datetime, time


TRIP_ID_IND = 0
ARRIVAL_TIME_IND = 1
DEPARTURE_TIME_IND = 2
STOP_ID_IND = 3
STOP_SEQUENCE_IND = 4
PICKUP_TYPE_IND = 5
DROP_OFF_TYPE_IND = 6

# class Stop:
    # def __init__(self, sid):

class Trip:
    def __init__(self, tid):
        self._id = tid
        self._stops = {}

    def add_stop(self, line):
        line = line.split(",")
        sid = int( line[STOP_ID_IND] )
        seq = int ( line[STOP_SEQUENCE_IND] )
        val = (sid, line[DEPARTURE_TIME_IND], line[ARRIVAL_TIME_IND])

        self._stops[seq] = val

    def get_duration(self):
        start_ind = min(self._stops)
        end_ind = max(self._stops)

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

        return time.strftime( '%H:%M:%S', time.gmtime(duration_sec) )


    def __str__(self):
        res  = "Trip ID: %s, #Stops= %d\n" % (self._id, len(self._stops) )
        for v in self._stops:
            res+= "%s -> %s\n"%(str(v), str(self._stops[v]))
        res += "Trip Duration: %s"%str( self.get_duration() )
        return res


all_trips = {}
def add_trip(tid, trips):
    if tid in trips: return
    trips[tid]  = Trip(tid)

def parse_line(line, trips):
    tid = line.split(",")[0]
    add_trip(tid, trips)
    trips[tid].add_stop(line)

start = time.clock()

with open("stop_times.txt",'r') as f:
    for line in f.readlines()[1:]:
        parse_line(line,all_trips)

ttl  = time.clock() - start
print time.strftime( '%H:%M:%S', time.gmtime(ttl) )

# for trip in all_trips:
    # print all_trips[trip]
#
