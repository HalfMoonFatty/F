'''
Problem:

Remove target char from source string. Move the target char to the end of the source string.

'''

'''
Solution:

Traverse the string and put the non-target character into the char array one by one, and put the target character at the end.

'''

def removeChar(s, target):
    s = list(s)
    slow = fast = 0
    while fast < len(s):
        # skip first several valid chars
        while slow < len(s) and s[slow] != target:
            slow += 1

        fast = slow
        while fast < len(s) and s[fast] == target:
            fast += 1

        while fast < len(s) and s[fast] != target:
            s[slow] = s[fast]
            s[fast] = target    # set fast to target 
            slow += 1
            fast += 1


    return ''.join(s[:slow])

s = 'abbcdbbafsjo'
target = 'b'
print removeChar(s, target)
