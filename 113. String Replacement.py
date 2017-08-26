'''
Problem:

  给一个字符串，如果是相邻字母是一样的话就称为一个桥，把桥之间的字符替换成加号
  e.g. --a-d*-d-a-b 变成 --a-++++-a-b
'''

import string
def replaceStr(s):
    s = list(s)
    i = 0
    while i < len(s)-1:
        j = i+1
        while not s[j].isalpha():
            j += 1
        if s[i] == s[j] and j > i+1:
            s[i:j+1] = '+' * (j-i+1)
            i = j + 1
        else: 
            i += 1
    return ''.join(s)

test = '--a-d*-d-a-b'
print replaceStr(test)
