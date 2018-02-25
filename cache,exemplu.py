import datetime
import random


########################################################################
class MyCache:
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.cache = {}
        self.max_cache_size = 10

    # ----------------------------------------------------------------------
    def __contains__(self, key):
        """
        Returns True or False depending on whether or not the key is in the
        cache
        """
        return key in self.cache

    # ----------------------------------------------------------------------
    def update(self, key, value):
        """
        Update the cache dictionary and optionally remove the oldest item
        """
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self.remove_oldest()

        self.cache[key] = {'date_accessed': datetime.datetime.now(),
                           'value': value}

    # ----------------------------------------------------------------------
    def remove_oldest(self):
        """
        Remove the entry that has the oldest accessed date
        """
        oldest_entry = None
        for key in self.cache:
            if oldest_entry is None:
                oldest_entry = key
            elif self.cache[key]['date_accessed'] < self.cache[oldest_entry][
                'date_accessed']:
                oldest_entry = key
        self.cache.pop(oldest_entry)

    # ----------------------------------------------------------------------
    @property
    def size(self):
        """
        Return the size of the cache
        """
        return len(self.cache)
if __name__ == '__main__':
    # Test the cache
    keys = ['test', 'red', 'fox', 'fence', 'junk',
            'other', 'alpha', 'bravo', 'cal', 'devo',
            'ele']
    s = 'abcdefghijklmnop'
    cache = MyCache()
    for i, key in enumerate(keys):
        if key in cache:
            continue
        else:
            value = ''.join([random.choice(s) for i in range(20)])
            cache.update(key, value)
        print("#%s iterations, #%s cached entries" % (i+1, cache.size))
        
        #1 iterations, #1 cached entries
#2 iterations, #2 cached entries
#3 iterations, #3 cached entries
#4 iterations, #4 cached entries
#5 iterations, #5 cached entries
#6 iterations, #6 cached entries
#7 iterations, #7 cached entries
#8 iterations, #8 cached entries
#9 iterations, #9 cached entries
#10 iterations, #10 cached entries
#11 iterations, #10 cached entries
