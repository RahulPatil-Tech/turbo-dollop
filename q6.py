class Solution(object):
	def maximumProduct(self, nums):
		nums.sort()
		return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
print(Solution().maximumProduct([1,2,3]))
print(Solution().maximumProduct([1,2,3,4]))
print(Solution().maximumProduct([-1,-2,-3]))
