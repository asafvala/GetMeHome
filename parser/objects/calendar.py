
class Service:
    def __init__(self, sid, operating, start_date, end_date):
        self._sid = sid
        self._operating = [int(v) for v in operating]
        self._start_date = start_date.strip()
        self._end_date = end_date.strip()

    def get_id(self):
        return self._sid

    def operating_on(self,day):
        return self._operating[day]

    def get_start_date(self):
        return self._start_date

    def get_start_year(self):
        return self._get_year(self._start_date)

    def get_start_month(self):
        return self._get_month(self._start_date)

    def get_start_day(self):
        return self._get_day(self._start_date)

    def get_end_year(self):
        return self._get_year(self._end_date)

    def get_end_month(self):
        return self._get_month(self._end_date)

    def get_end_day(self):
        return self._get_day(self._end_date)

    def _get_year(self, val):
        return int(val[:4])

    def _get_month(self, val):
        return int(val[4:6])

    def _get_day(self, val):
        return int(val[6:])

class SerivcesParser:
    def __init__(self):
        self._services = {}

    def _init_service(self, sid,operating,start,end):
        if sid in self._services: return
        self._services[sid] = Service(sid,operating,start,end)

    def parse(self, fname):
        with open(fname, 'r') as f:
            next(f)
            for line in f:
                vals = line.split(',')
                self._init_service(vals[0], ''.join(vals[1:8]),vals[8],vals[9])

    def get(self):
        return self._services
