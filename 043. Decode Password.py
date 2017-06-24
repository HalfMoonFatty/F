'''
Problem: 破解密码

提供一个函数 isPassword(String str), 如果pass in的是正确的密码，return True。
又给定了每个字母可以变形的集合（例如，字母a可以变形为a或者A或者B或者*，字母b可以变形为B或者F或者&...，需要自己设计一个data structure来存这个mapping)。
设计并实现一个函数，在给定一个字符串的情况下，对字符串进行变形，最后找到正确的密码。

'''

'''
Solution: Phone Number Letter Combination

Time O(3^n)
Space O(3^n)
'''

class Solution(object):
    def letterCombinations(self, digits):
        
        def dfs(digits, index, res, result):
            if index == len(digits):    # index == len(digits) and if isPassword(res)
                result.append(res)
                return
            
            for char in mp[digits[index]]:
                dfs(digits, index+1, res+char, result)
            return
        
                
        if not digits: return []     
        mp = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        dfs(digits, 0, '', result)
        return result
