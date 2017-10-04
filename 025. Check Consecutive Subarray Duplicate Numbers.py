'''
Problem:

给一个array, 然后给 个k, 让你check连续的k个integer是否含有dulplicate。

很简单的， 窗口为K的hashset一直扫一遍就行了。  
'''


def containsNearbyDuplicate(nums, k):
    i = j = 0
    window = set()
    while j < len(nums):
        if j - i + 1 > k:  # window size = j - i + 1
            window.remove(nums[i])
            i += 1
        if nums[j] in window:
            return True
        window.add(nums[j])
        j += 1
    return False


nums = [1,2,3,2,1,4]
print containsNearbyDuplicate(nums, 3)




def containsNearbyDuplicate(nums, k):
    i = j = 0
    window = set()
    while j < len(nums):
        while j - i + 1 <= k:  # window size = j - i + 1
            if nums[j] in window:
                return True
            window.add(nums[j])
            j += 1

        window.remove(nums[i])
        i += 1
    return False


nums = [1,2,3,2,1,4]
print containsNearbyDuplicate(nums, 3)





