'''
Problem 1: Random Pick Index 2D

Randomly pick K points in a l*w matrix.

'''

'''
Solution: reversior smaple

Use a array to store the points we fetch out

For the first k points in matrix, put into array. 
For k + 1 ~ end points, we creat a random number j in range [0, index]. If this j is smaller than k, then we chooes this point instead the points[j]


Prove the possibility:

For points index after k, if we eventually choose this point, which means after this point no other points can replace it in the reversior, 
the random number can be any number but not this point's index, which means their possibility is (index - 1 / index)
So the posibility is: (k / index) * (index / index + 1) * (index + 1 / index + 2)....* (n - 1 / n) = (k / n)
                           |                |               
 选中在reversior中的一个去 replace   从index+1个中选index个数就是不能选这个数来替代


For points index smaller than k, if we eventually choose this point, no points can replace it, 
so the possibility is (k / k + 1) * (k + 1 / k + 2) * ......* (n - 1 / n) = (k / n)
'''



import random
def randomKPoints2D(matrix,k):

    m,n = len(matrix), len(matrix[0])
    
    if k > m*n: return

    points = [0]*k   # reversior
    # put the first k elements in the reversior
    for i in range(k): 
        points[i] = [i/n, i%n]
        matrix[i/n][i%n] = 1

    for i in range(k, m*n):
        j = random.randint(0,i)
        if j < k:
            matrix[points[j][0]][points[j][1]] = 0
            ni,nj = i/n, i%n
            matrix[ni][nj] = 1
            points[j] = [ni,nj]
    return



matrix = [[0] * 5 for _ in range(5)]
k = 5
randomKPoints2D(matrix,k)
print matrix





'''
Problem 2: 398. Random Pick Index

Given an array of integers with possible duplicates, randomly output the index of a given target number. 
You can assume that the given target number must exist in the array.
Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.
Example:
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);
// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);
// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
'''

'''
For the nth target, ++count is n. Then the probability that rnd.nextInt(++count)==0 is 1/n. Thus, the probability that return nth target is 1/n.
For (n-1)th target, the probability of returning it is (n-1)/n * 1/(n-1)= 1/n.
'''

class Solution(object):

    def __init__(self, nums):
        
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index = -1
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0,count) == 0:
                    index = i
                count += 1
                    
        return index


      

'''
Problem 3: 382. Linked List Random Node
   
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.
   
Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?
   
Example:
   
// Init a singly linked list [1,2,3].
// getRandom() should return either 1, 2, or 3 randomly.
// Each element should have equal probability of returning.
// solution.getRandom();
'''

'''
Solution:

Choose k entries from n numbers. Make sure each number is selected with the probability of k/n
BASIC IDEA:
Choose 1, 2, 3, ..., k first and put them into the reservoir.
For k+1, pick it with a probability of k/(k+1), and randomly replace a number in the reservoir.
For k+i, pick it with a probability of k/(k+i), and randomly replace a number in the reservoir.
Repeat until k+i reaches n
PROOF:
For k+i, the probability that it is selected and will replace a number in the reservoir is k/(k+i)
For a number in the reservoir before (let's say X), the probability that it keeps staying in the reservoir is
P(X was in the reservoir last time) * P(X is not replaced by k+i)
= P(X was in the reservoir last time) * (1- P(X is replaced this time))
= k/(k+i-1) * (1 - k/(k+i) * 1/k) = k/(k+i)
When k+i reaches n, the probability of each number staying in the reservoir is k/n
'''


class Solution(object):
   
    def __init__(self, head):

        self.head = head
   
    def getRandom(self):

        def getRandK(k):
            cur = self.head
            res = [0]*k
            i = 0
           
            # init res with first k vals
            while cur and i < k:
                res[i] = cur.val
                cur = cur.next
                i += 1
           
            while cur:
                j = random.randint(0,i)
                if j < k:
                    res[j] = cur.val
                cur = cur.next
                i += 1
           
            return res
       
        return getRandK(1)[0]
      
      
      
      

'''
Problem 4: 384. Shuffle an Array

    Shuffle a set of numbers without duplicates.
    Example:
    // Init an array with set 1, 2, and 3.
    int[] nums = {1,2,3};
    Solution solution = new Solution(nums);
    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
    solution.shuffle();
    // Resets the array back to its original configuration [1,2,3].
    solution.reset();
    // Returns the random shuffling of array [1,2,3].
    solution.shuffle();
'''


'''
Solution:

i from back to front, randomly select an index j to swap with i.
Time O(n)
Space O(n)
proof the possiblity that any permutation is equally likely to be returned.
suppose we have an array:
+-------------------------------------+
|_____|_________________|_____________|
      j                 i            n-1
possibility of swapping i and j is:
P(i,j swapped)
= P(j swap with i | j not swapped for [i+1,n])
= 1/i * (1-1/n) * (1-1/n-1) * (1-1/n-2) ... * i/i+1
= 1/i * n-1/n * n-2/n-1 * ... * i/i+1
= 1/n
'''

class Solution(object):

    def __init__(self, nums):
        self.nums = nums


    def reset(self):
        return self.nums


    def shuffle(self):
        res = self.nums[:]
        for i in range(len(res)-1,-1,-1):
            j = random.randint(0,i)
            res[i],res[j] = res[j],res[i]
        return res
