'''
Problem:

    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    You are given a target value to search. If found in the array return its index, otherwise return -1.
   
    You may assume no duplicate exists in the array.
'''

        |
        |／│
      ／|  │
    ／  |  │
  ／    |  │  
 │  ②   |① │  ／│ 
 │      |  │／③ │ 
 -------|--------
 s     mid      e



          |
    ／│   |
  ／  │   |
 │    │   |    ／│
 │    │   |  ／  │
 │  ③ │   |／    │
 │    │／①|   ②  │
----------|--------
 s       mid    e






# Solution 1: Binary Search - Iteration Solution

class Solution(object):
   
    def search(self, nums, target):

        def BinarySearch(nums,s,e,tar):
            while s <= e:
            
                mid = s + (e - s)/2
                
                if tar == nums[mid]:
                    return mid
               
                if nums[mid] >= nums[s]:   # >=
                    if tar > nums[mid]:
                        s = mid + 1
                    elif tar >= nums[s]:
                        e = mid - 1
                    else:
                        s = mid + 1
                        
                else:
                    if tar < nums[mid]:
                        e = mid - 1
                    elif tar <= nums[e]:    # <=
                        s = mid + 1
                    else:
                        e = mid - 1
       
            return -1
                
        
        if not nums: return -1
        return BinarySearch(nums,0,len(nums)-1,target)




# Solution 2: Binary Search - Recursive Solution


class Solution(object):
   
    def search(self, nums, target):

        def helper (nums,s,e,tar):
            if s > e:
                return -1
           
            mid = s + (e - s)/2
           
            if tar == nums[mid]:
                return mid
       
            if nums[mid] >= nums[s]:    # >=
                if tar > nums[mid]:
                    s = mid + 1
                elif tar >= nums[s]:    # >=
                    e = mid - 1
                else:
                    s = mid + 1
           
            elif tar < nums[mid]:
                e = mid - 1

            elif tar <= nums[e]:    # <=
                s = mid + 1
           
            else:
                e = mid - 1
       
            return helper (nums,s,e,tar)
       
       
        end = len(nums)-1
        start = 0
        return helper(nums,start,end,target)

    
'''
Problem:
    Follow up for "Search in Rotated Sorted Array":
    What if duplicates are allowed?
    Would this affect the run-time complexity? How and why?
    Write a function to determine if a given target is in the array.
'''


# Solution: If duplicates are allowed, the only way to search is linear scan, so run-time is O(n)

 class Solution(object):
   
    def search(self, nums, target):
       
        for elem in nums:
            if elem == target:
                return True
        return False
