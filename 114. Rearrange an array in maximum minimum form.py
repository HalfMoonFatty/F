'''
Problem:

Given an unsorted array, sort it in such a way that the first element is the largest value, the second element is the smallest, 
the third element is the second largest element and so on. 

[2, 4, 3, 5, 1] -> [5, 1, 4, 2, 3] 
can you do it without using extra space 
public void sortAlternate(int[] nums){}

Geeks for Geeks:

Given a sorted array of positive integers, rearrange the array alternately i.e first element should be maximum value, 
second minimum value, third second max, fourth second min and so on.

Examples:

Input  : arr[] = {1, 2, 3, 4, 5, 6, 7} 
Output : arr[] = {7, 1, 6, 2, 5, 3, 4}

Input  : arr[] = {1, 2, 3, 4, 5, 6} 
Output : arr[] = {6, 1, 5, 2, 4, 3}
Expected time complexity is O(n).
'''


'''
Solution 1:
Time: O(n)
Space: O(n)
'''

def rearrange(arr, n):

    result = [None] * n
    small,large = 0,n-1

    for i in range(n):
        if i%2 == 0:
            result[i] = arr[large]
            large -= 1
        else:
            result[i] = arr[small]
            small += 1
 
    return result


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print "Original Array", arr    # Original Array [1, 2, 3, 4, 5, 6, 7, 8, 9]
print "Modified Array", rearrange(arr, len(arr))    # Modified Array [9, 1, 8, 2, 7, 3, 6, 4, 5]



'''
Follow-up: Using O(1) extra space

How does expression “arr[i] += arr[max_index] % max_element * max_element” work ?

The purpose of this expression is to store two elements at index arr[i]. 

arr[max_index] is stored as multiplier and “arr[i]” is stored as remainder. 

For example in {1 2 3 4 5 6 7 8 9}, max_element is 10 and we store 91 at index 0. 

With 91, we can get original element as 91%10 and new element as 91/10.
'''
def rearrange(arr):

    n = len(arr)
    small, large = 0, n-1
    max_elem = arr[n-1] + 1

    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[large] % max_elem) * max_elem
            large -= 1
        else:
            arr[i] += (arr[small] % max_elem) * max_elem
            small += 1
    
    # arr = [91, 12, 83, 24, 75, 36, 67, 48, 59]
    for i in range(len(arr)):
        arr[i] /= max_elem

    return 


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print "Original Array", arr
rearrange(arr)
print "Modified Array", arr

