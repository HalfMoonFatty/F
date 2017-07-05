'''
Problem:

给定一个数组, 已经sort好, 里面有大量重复的数, 输出每个数和这个数出现的次数. 

输入[1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3]这样一个数组，返回{1, 4}, {2, 7}, {3, 10}

其实就是不同的数字要你计数，但是要求优于O(n)

先说扫一遍, 用hashmap计数, 问time complexity说是O(n), 不够好, 怎么快点儿, 答binary search. 

lz当时第一反应是binary search 找上下界，然后小哥问我worst case，我说O(nlgn)，小哥说对啊，我要优于O(n)。 

每次比较start point 和start point + 2^n位置上的数，假如一样就continue，不一样就在区间里面binary search找上界，这样的话worstcase O(n)

假设没有重复的数， [1,2,3,4,5] 每次都找 2^(n-1)  == 2^0 ==1 , 相当于依次 找1 找2 找3 找4 找5 发现都是出现一次， 遍历一遍， O(n). 

如果有大量重复， 【1，1，1，1，2，2，2，3】，对于1， 找右边界是 依次 尝试 2^0=1, 2^1 =2, 2^2=4, 2^3=8, O(nlogn)

每次都是尝试 start point +2^n 这样，也实现了 log(n) 的复杂度。

'''

def numberFreq(nums):

    def findLast(start):
        char = nums[start]
        dist = 1
        while start+dist < len(nums) and nums[start+dist] == char:
            dist *= 2
        if start + dist >= len(nums):    # note
            return len(nums)-1

        end = start + dist
        while start < end-1:    # note
            mid = start + (end-start)/2
            if nums[mid] == char:
                start = mid
            else:
                end = mid
        return start



    if not nums: return []
    result = []

    start = 0
    while start < len(nums):
        end = findLast(start)
        result.append([nums[start],end-start+1])
        start = end + 1

    return result


test = [1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3]
print numberFreq(test)
