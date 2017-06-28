'''
Problem 1:

Randomly pick K points in a l*w matrix.

'''

'''
Solution: reversior smaple

Use a array to store the points we fetch out

For the first k points in matrix, put into array. 
For k + 1 ~ end points, we creat a random number j in range [0, index]. If this j is smaller than k, then we chooes this point instead the points[j]


Prove the possibility:

For points index after k, if we eventually choose this point, which means after this point no other point can replace it in the reversior, 
the random number can be any number but not this point's indexwhich means their possibility is (index - 1 / index)
So the posibility is: (k / index) * (index / index + 1) * (index +1 / index + 2)....*(n - 1 / n) = (k / n)


// For points index smaller k, if we eventually choose this point,
// no points can replace it, so the possibility is (k / k + 1) * (k +
1 / k + 2) * ......* (n - 1 / n) = (k / n)
'''





'''
Problem 4:
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
