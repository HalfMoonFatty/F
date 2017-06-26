'''
Problem 1:
   
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
   
For example, given
s = "leetcode",
dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code".
'''

# Solution 1 DP
class Solution(object):
    def wordBreak(self, s, wordDict):
       
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i-1,-1,-1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
       
        return dp[-1]
        
		
    
   
# Solution 2 Backtracking
class Solution(object):
    def wordBreak(self, s, wordDict):
       
        def dfs(start, s, wordDict):
            if start == len(s): return True
                
            for i in range(start+1,len(s)+1):
                if s[start:i] in wordDict:
                    if dfs(i,s,wordDict):
                        return True
                
            return False
       
        return dfs(0,s,wordDict)
        
        
        
'''
Problem 2:

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].
A solution is ["cats and dog", "cat sand dog"].
'''

# Solution 1: DFS+ Cache

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def dfs(s, wordDict, cache):
            if cache.has_key(s): return cache[s]
            if not s: return []
            
            result = []
            for length in range(1,len(s)+1):
                word = s[0:length]
                if word in wordDict:
                    if length == len(s): 
                        result.append(word)
                    else:
                        ret = dfs(s[length:], wordDict, cache)
                        for item in ret:
                            result.append(word + " " + item)
                            
            cache[s] = result
            return result
            
        return dfs(s, wordDict, {})
