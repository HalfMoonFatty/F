import collections

def findSubstring(s, t):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if not s or len(t) > s: return []
    
    result = []
    char_count = collections.Counter(t)

    for i in range(len(s) - len(t) + 1):
        char_map = {}
        extraword = False
        for j in range(i,i+len(t)):
            char_map[s[j]] = char_map.get(s[j],0)+1
            if char_map[s[j]] > char_count.get(s[j],0):
                extraword = True
                break
        
        if not extraword:
            result.append(i)
    return result 


S = "ADOBECODEBANCAB"
T = "ABC"
print findSubstring(S,T)
