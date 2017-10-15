class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K: sum_ -= nums[i-K]
            if i >= K-1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in xrange(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] >
                    W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans







import sys
def max3Ksum(nums, k):
	n = len(nums)
	if not nums or n < 3*k: 
		return 0

	left = [0] * n    # left[i] is the value from the left includes nums[i]
	right = [0] * n   # right[i] is the value from the right excludes nums[i]
	ans = -sys.maxint-1

	wsums = 0
	for i in range(n-2*k):
		wsums += nums[i]
		if i >= k: wsums -= nums[i - k]
		if i >= k - 1: left[i+1] = max(left[i],wsums)
	print left

	wsums = 0
	for i in range(n-1,2*k,-1):
		wsums += nums[i]
		if i <= n - k - 1: wsums -= nums[i+k]
		if i <= n - k: right[i-1] = max(right[i],wsums)
	print right

	wsums = 0
	cursum = 0
	for i in range(k,n-k):
		wsums += nums[i]
		if i > k + 1: wsums -= nums[i - k]
		if i > k: cursum = max(cursum,wsums)
		ans = max(ans, left[i-1] + cursum + right[i])

	return ans


nums = [1,1,100,100,1,1,100,100,1,1,100,100]
nums = [0,1,2,3,4,5,6]
print max3Ksum(nums,2)
