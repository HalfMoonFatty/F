'''
Problem: Remove Duplicate Chars in a String

'''

import collections

def removeDup(s):
    result = []
    count = collections.Counter(s)
    for k,v in count.items():
        if v == 1:
            result.append(k)
    return ''.join(result)


s = 'abcab'
print removeDup(s)
