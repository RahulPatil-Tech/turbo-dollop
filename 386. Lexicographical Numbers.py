'''
386. Lexicographical Numbers
Medium
Topics
premium lock icon
Companies
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
'''
# Depth-First Search Trie
# Solution();
class Solution(object):
    def lexicalOrder(self, n: int) -> list[int]:
        res = []
        def dfs(node):
            if node > n:
                return
            res.append(node)
            for i in range(10):
                n_num = node * 10 + i
                if n_num > n:
                    break
                dfs(n_num)
        for i in range(1, 10):
            if i <= n:
                dfs(i)
            else:
                break
        return res
print(Solution().lexicalOrder(n = 13))
print(Solution().lexicalOrder(n = 2))