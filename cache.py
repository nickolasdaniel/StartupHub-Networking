import re
import datetime
import collections

class Entry(object):

    def __init__(self, content, req_datetime):
        self.content = content
        self.req_datetime = req_datetime

    def __str__(self):
        return "Content: {}\n Number of bytes: {}\n Date: {}\n".format(self.content, len(self.content), self.req_datetime)


class WebCacheProxy(object):
    def __init__(self, limit=10):
        self.limit = limit
        self.dict = {}

    def __contains__(self, key):
        return key in self.dict

    def add_entry_cache(self, key, value):
        if len(self.dict) >= self.limit and key not in self.dict:
            self.remove_entry_cache()
        self.dict[key] = value

    def remove_entry_cache(self):
        auxkey = None
        for key, value in self.dict.items():
            if auxkey is None:
                auxkey = key

            elif value.req_datetime < self.dict[auxkey]:
                auxkey = key

        del self.dict[auxkey]

    # def get_entry_cache(self, key):
    #     http_pattern = re.compile("htt[ps]://[a-zA-Z0-9].[a-z]{3} +")
    #     if key not in self.dict and http_pattern.search(key) is None:
    #         raise KeyError('Request not in cache or doesn`t match the pattern')
    #     return self.dict[key]

    def number_of_elements(self):
        return len(self.dict)

if __name__ == '__main__':
    e = Entry('http://index.html', datetime.datetime.now())
    print(e)
