import re
import datetime
import collections

url='http://www.google.com/index.html'
class Entry(object):

    def __init__(self, content, req_datetime):
        self.content=content
        self.req_datetime=req_datetime


    def __str__(self):
        pass


class WebCacheProxy(object):
    def __init__(self, limit=10):
        self.limit=limit
        self.dict = {}

    def __contains__(self, key):
        return key in self.dict

    def __str__(self):
        pass

    def add_entry_cache(self, key, value):
        if len(self.dict) >= self.limit and key not in self.dict:
            self.remove_entry_cache()
        self.dict[key] = {"date_accesed": datetime.datetime.now(),'value':value}

    def remove_entry_cache(self):
        auxkey = None
        for key,value in self.dict.items():
            if auxkey is None:
                auxkey=key

            elif self.dict[key]['date_accesed']<self.dict[auxkey]['date_accesed']
                auxkey=key

        self.dict.pop(auxkey)

    def get_entry_cache(self, key):
        pass

