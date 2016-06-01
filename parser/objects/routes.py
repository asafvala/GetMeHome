import pandas as pd
from parser import consts

class Route:
    def __init__(self, rid,operator,rtype,rname,route_desc,rcolor):
        self._rid = rid # This would hold all of the routes options
        self._rname = rname
        self._operator = operator
        self._rtype = rtype
        self._rcolor = rcolor
        self._route_desc = route_desc

class MetaRoute:
    def __init__(self, rid,operator,rtype,rname,route_desc,rcolor):
        self._options = [(rid,route_desc)] # This would hold all of the routes options
        self._rname = rname
        self._operator = operator
        self._rtype = rtype
        self._rcolor = rcolor

    def add_option(self, rid, route_desc):
        self._options.append( (rid,route_desc)  )

    def get_options(self):
        return self._options

    @staticmethod
    def parse_description(desc):
        return desc.split("-")


class RoutesParser:

    def __init__(self):
        self._routes = {}
        self._meta_routes = {}

    def _init_route(self, rid, operator, rtype, rname, route_desc, rcolor):
        if rid not in self._routes:
            self._routes[rid] = Route(rid,operator,rtype,rname,route_desc,rcolor)

        if rname in self._meta_routes:
            self._meta_routes[rname].add_option(rid,route_desc)
        else:
            self._meta_routes[rname] = MetaRoute(rid,operator,rtype,rname,route_desc,rcolor)

    def parse(self, routes_file):
        self._init_all_routes(routes_file)

    def get(self):
        return self._routes, self._meta_routes

    def _init_all_routes(self, fname):
        f = pd.read_csv(fname)
        num_routes = len(f[consts.RoutesFileHeaders.ROUTE_ID])

        for route_ind in range(num_routes):
            # we only do bus routes for now
            if f[consts.RoutesFileHeaders.ROUTE_TYPE][route_ind] == \
                            consts.RoutesFileHeaders.BUS_TYPE_VAL:

                rid = f[consts.RoutesFileHeaders.ROUTE_ID][route_ind]
                operator = f[consts.RoutesFileHeaders.AGENCY_ID][route_ind]
                rtype = f[consts.RoutesFileHeaders.ROUTE_TYPE][route_ind]
                rname = f[consts.RoutesFileHeaders.SHORT_NAME][route_ind]
                route_desc = f[consts.RoutesFileHeaders.ROUTE_DESC][route_ind]
                rcolor = f[consts.RoutesFileHeaders.ROUTE_COLOR][route_ind]
                self._init_route(rid, operator, rtype, rname, route_desc, rcolor)
