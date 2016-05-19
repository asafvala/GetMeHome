class StopTimesIndeces:
    TRIP_ID_IND = 0
    ARRIVAL_TIME_IND = 1
    DEPARTURE_TIME_IND = 2
    STOP_ID_IND = 3
    STOP_SEQUENCE_IND = 4
    PICKUP_TYPE_IND = 5
    DROP_OFF_TYPE_IND = 6

class FileNames:
    ROUTES = "routes.txt"
    STOPS = "stops.txt"
    STOP_TIME = "stop_times.txt"


class StopsFileHeaders:
    STOP_ID = u'stop_id'
    STOP_CODE = u'stop_code'
    STOP_NAME = u'stop_name'
    STOP_DESC = u'stop_desc'
    STOP_LAT = u'stop_lat'
    STOP_LONG = u'stop_lon'
    STOP_LOCATION = u'location_type'
    STOP_PARENT = u'parent_station'
    STOP_ZONE_ID = u'zone_id'

class RoutesFileHeaders:
    ROUTE_ID = u'route_id'
    AGENCY_ID = u'agency_id'
    SHORT_NAME = u'route_short_name'
    LONG_NAME = u'route_long_name'
    ROUTE_DESC = u'route_desc'
    ROUTE_TYPE = u'route_type'
    ROUTE_COLOR = u'route_color'

    BUS_TYPE_VAL = 3
