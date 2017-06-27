'''
Problem: 

You have a string of numbers, i.e. 123. You can insert a + or - sign in front of ever number, or you can leave it empty. 
Find all of the different possibilities, make the calculation and return the sum. 

For example; 
+1+2+3 = 6 
+12+3 = 15 
+123 = 123 
+1+23 = 24 
... 
-1-2-3 = 6 
... 
Return the sum of all the results.

'''

def addOperator(number):

    def helper(number, index, res, result):
        if index == len(number):
            result.add(eval(res[:]))
            return

        for i in range(index, len(number)):
            if i != index and number[index] == '0':    # note: leading '0'
                return
            num = number[index:i+1]
            helper(number, i+1, res + "+" + num, result)
            helper(number, i+1, res + "-" + num, result)

    result = set()
    helper(number, 0, '', result)
    return list(result)

print addOperator('103')  
