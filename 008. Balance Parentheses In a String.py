'''
Problem:

You have a string consisting of open and closed parentheses, but parentheses may be imbalanced. 
Make the parentheses balanced and return the new string.

例子：
"(a)()" -> "(a)()"
"((bc)" -> "(bc)"
")))a((" -> "a"
"(a(b)" ->"(ab)" or "a(b)"

Note: balance的意思就是把原来string里unpaired的括号变成paired的形式。
如果有多个可能的结果， 比如上述最后一种情况，我们就只需要输出一个对的结果即可，所以这点简化了题目的难度。
'''


'''
Solution:

Do 2 rounds of scans with a counter on open parens first and one with a counter on close parens. 

The first scan finds all unmatched close parens and the second one finds all unmatched open parens. 

First loop traverse from left to right, use a counter to count the valid parenthese, meet '(' +1, meet ')' if count > 0 -1, 
else delete this ')'. Then all the invalid ')' will be deleted

Second loop traverse from right to left. also use a counter to count valid parenthese meet ')' +1. Then all the invalid '(' will be deleted.

Time complexity: O(n), space complexity: O(n)
'''

def balanceParentheses(s):

    def deleteCloseParenthes(s):
        count = 0
        result = []
        for char in s:    # from left to right
            result.append(char)
            if char == "(":
                count += 1
            elif char == ")":
                if count > 0: count -= 1
                else: result.pop()
        return ''.join(result)


    def deleteOpenParenthes(s):
        count = 0
        result = []
        for i in range(len(s)-1,-1,-1):   # from right to left
            result.append(s[i])
            if s[i] == ")":
                count += 1
            elif s[i] == "(":
                if count > 0: count -= 1
                else: result.pop()
        return ''.join(result[::-1])    # reverse result



    result = ''
    result = deleteCloseParenthes(s)
    result = deleteOpenParenthes(result)
    return result


test = ["(a)()", "((bc)", ")))a((", "(a(b)"]
for t in test:
    print balanceParentheses(t)

