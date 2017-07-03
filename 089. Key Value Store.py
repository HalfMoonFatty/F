'''
Problem:

implement 4 methods of a key value store data structure: 

add(key, value), remove(key), get(key), lastestKey()(return last visited key)

'''

class KeyValueStore(object):

    def __init__(self, capacity):
        self.cache = collections.deque([])    # store keys
        self.cacheMap = {}                    # store key-value pairs


    def add(self, key, value):
        # if key exist
        if self.cacheMap.has_key(key):
            self.cache.remove(key)
        # both case: key exist or not
        self.cache.append(key)
        self.cacheMap[key] = value
        
        
    def remove(self, key):
        if not self.cacheMap.has_key(key):
            return False
        self.cache.remove(key)
        del self.cacheMap[key]
        return True


    def get(self, key):
        if self.cacheMap.has_key(key):
            # note: remove and append to tail
            self.cache.remove(key)
            self.cache.append(key)
            return self.cacheMap[key]
        else:
            return -1


    def lastKey(self):
        return self.cache[-1]
