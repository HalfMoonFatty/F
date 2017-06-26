'''
Problem:

string 比较的时候考虑里面数字的大小，char 比 digit重要 

e.g. abc9 < abc123 abc > ab9  
'''

def strComparator(s1, s2):
    index1, index2 = 0, 0 
    while index1 < len(s1) and index2 < len(s2):
        # both are SAME alphabet 
        if s1[index1] == s2[index2] and s1[index1].isalpha():
            index1 += 1
            index2 += 1
        # both are digits
        elif s1[index1].isdigit() and s2[index2].isdigit():
            n1 = n2 = 0
            while index1 < len(s1):
                n1 += int(s1[index1])
                n1 *= 10
                index1 += 1
            while index2 < len(s2):
                n2 += int(s2[index2])
                n2 *= 10
                index2 += 1
            if n1 < n2: return -1
            elif n1 == n2: return 0
            else: return 1

        # s1 is digit
        elif s1[index1].isdigit(): return -1
        # s2 is digit
        elif s2[index2].isdigit(): return 1
        # s1 and s2 are both char
        elif s1[index1] > s2[index2]: return 1
        else: return -1



s1 = 'abc9'
s2 = 'abc123'
print strComparator(s1,s2)

s1 = 'abc'
s2 = 'ab9'
print strComparator(s1,s2)


