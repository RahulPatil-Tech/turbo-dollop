'''

440. K-th Smallest in Lexicographical Order
Hard
Topics
premium lock icon
Companies
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109
'''
# Solution(): Trie
from sys import prefix


class Solution():
    def findKthNumber(self, n: int, k: int) -> int:
        def count(node, n):
            """Return the number of nodes in the range [node, n]"""
            count = 0
            curr= node
            next_curr= node + 1
            while curr <= n:
                count += min(n + 1, next_curr)-curr
                curr *= 10
                next_curr *= 10
            return count
        current = 1
        k -= 1
        while k > 0:
            num_nodes = count(current, n)
            if k >= num_nodes:
                current += 1
                k -= num_nodes
            else:
                current *= 10
                k -= 1
        return current
print(Solution().findKthNumber( n = 13, k = 2))# Expected 10
print(Solution().findKthNumber( n = 1, k = 1)) # Expected 1 
        