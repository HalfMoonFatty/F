'''
Problem: Permutaions

Given a collection of numbers, return all possible permutations.
For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''



class Solution(object):
    def permute(self, nums):

        def permuteHelper(nums, index, result):
            if index == len(nums):
                result.append(nums)
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                permuteHelper(nums[:], index+1, result)
                nums[index], nums[i] = nums[i], nums[index]
            return 


        result = []
        permuteHelper(nums, 0, result)
        return result

    
    
    
'''
Problem 2: Unique Permutations

Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''



from sets import Set
class Solution(object):
    def permuteUnique(self, nums):

        def permuteUniqueHelper(nums, index, path, result):
            if index == len(nums):
                result.append(nums)
                return
            for i in range(index, len(nums)):
                if nums[i] not in path:
                    path.add(nums[i])    # add the current number to the hashset
                    nums[index], nums[i] = nums[i], nums[index]
                    permuteUniqueHelper(nums[:], index+1, Set(), result)
                    nums[index], nums[i] = nums[i], nums[index]
            return


        result = []
        permuteUniqueHelper(nums, 0, Set(), result)
        return result
    
    
    
    
    
'''
Problem 3: 

A "derangement" of a sequence is a permutation where no element appears in its original position. 
For example ECABD is a derangement of ABCDE, given a string, may contain duplicate char, please out put all the derangement 
public List<char[]> getDerangement(char[]){}. 

'''

def derangement(s):
    def isValid(s, ns):
        for i in range(len(s)):
            if s[i] == ns[i]:
                return False
        return True


    def helper(index, ls, path, result):
        if index == len(ls) and isValid(s,ls):
            result.append(''.join(ls))
            return
        for i in range(index, len(ls)):
            if ls[i] not in path:
                path.add(ls[i])
                ls[index], ls[i] = ls[i], ls[index]
                helper(index+1, ls[:], set(), result)
                ls[index], ls[i] = ls[i], ls[index]
        return

    result = []
    helper(0,list(s),set(), result)
    return result


s = 'ABCDE'
print derangement(s)

