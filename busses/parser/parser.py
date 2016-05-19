from 

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
