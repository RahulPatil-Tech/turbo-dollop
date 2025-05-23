'''
3068. Find the Maximum Sum of Node Values
Solved
Hard
Topics
Companies
Hint
There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
nums[u] = nums[u] XOR k
nums[v] = nums[v] XOR k
Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.

 

Example 1:


Input: nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]
Output: 6
Explanation: Alice can achieve the maximum sum of 6 using a single operation:
- Choose the edge [0,2]. nums[0] and nums[2] become: 1 XOR 3 = 2, and the array nums becomes: [1,2,1] -> [2,2,2].
The total sum of values is 2 + 2 + 2 = 6.
It can be shown that 6 is the maximum achievable sum of values.
Example 2:


Input: nums = [2,3], k = 7, edges = [[0,1]]
Output: 9
Explanation: Alice can achieve the maximum sum of 9 using a single operation:
- Choose the edge [0,1]. nums[0] becomes: 2 XOR 7 = 5 and nums[1] become: 3 XOR 7 = 4, and the array nums becomes: [2,3] -> [5,4].
The total sum of values is 5 + 4 = 9.
It can be shown that 9 is the maximum achievable sum of values.
Example 3:


Input: nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]
Output: 42
Explanation: The maximum achievable sum is 42 which can be achieved by Alice performing no operations.
 

Constraints:

2 <= n == nums.length <= 2 * 104
1 <= k <= 109
0 <= nums[i] <= 109
edges.length == n - 1
edges[i].length == 2
0 <= edges[i][0], edges[i][1] <= n - 1
The input is generated such that edges represent a valid tree.'''
# Solution : with Collection: 
from math import inf
import time
class Solution():
    def maximumValueSum(self, nums, k, edges):
        change = 0
        min_s = inf
        final = 0
        for val in nums:
            temp = val ^ k
            if temp > val:
                change += 1
                final += temp
                min_s = min(min_s, temp-val)
            else:
                final += val
                min_s = min(min_s, val-temp)
        if change % 2 :
            final -= min_s
        return final
    
start_time = time.time()
print(Solution().maximumValueSum(nums = [2,3], k = 7, edges = [[0,1]]))
print(Solution().maximumValueSum( nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]))
end_time = time.time()
print(f"\nExecution time: {end_time - start_time:.6f} seconds")

# Approach 
from collections import deque
class Solution1:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        nums_deque = deque(nums)

        total_sum = 0
        num_beneficial_flips = 0
        min_abs_diff = inf

        for val in nums_deque:
            xored_val = val ^ k

            if xored_val > val:
                total_sum += xored_val
                num_beneficial_flips += 1
                min_abs_diff = min(min_abs_diff, xored_val - val)
            else:
                total_sum += val
                min_abs_diff = min(min_abs_diff, val - xored_val)

        if num_beneficial_flips % 2 != 0:
            total_sum -= min_abs_diff

        return int(total_sum)
start_time = time.time()
print(Solution1().maximumValueSum(nums = [2,3], k = 7, edges = [[0,1]]))
print(Solution1().maximumValueSum( nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]))
end_time = time.time()
print(f"\nExecution time: {end_time - start_time:.6f} seconds")
