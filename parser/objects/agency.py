import pandas
from parser import consts


class Agency:

    def __init__(self,aid,name):
        self._aid = int(aid)
        self._name = name

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def __str__(self):
        return "NAME: %s [AID: %d]"%(self._name, self._aid)

class AgencyParser:
    def __init__(self):
        self._agencies = {}

    def _init_all_agencies(self, agencies_file):
        with open(agencies_file, 'r') as f:
            next(f)
            for line in f:
                splitted = line.split(",")
                aid = splitted[consts.AgenciesIndeces.AGENCY_ID]
                name = splitted[consts.AgenciesIndeces.AGENCY_NAME]
                self._init_agency(aid, name)

    def _init_agency(self, aid, name):
        if aid in self._agencies: return
        self._agencies[aid] = Agency(aid,name)

    def parse(self, agencies_file):
        self._init_all_agencies(agencies_file)

    def get(self):
        return self._agencies
