'''
3170. Lexicographically Minimum String After Removing Stars
Medium
Topics
premium lock icon
Companies
You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

While there is a '*', do the following operation:

Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
Return the lexicographically smallest resulting string after removing all '*' characters.

 

Example 1:

Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.

Example 2:

Input: s = "abc"

Output: "abc"

Explanation:

There is no '*' in the string.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters and '*'.
The input is generated such that it is possible to delete all '*' characters.'''
# Solution(): Hash Table, String ,Stack , Greedy, Heap (Priority Queue)
import heapq
class Solution():
    def clearStars(self, s: str) -> str:
        n = len(s)
        stack = [False] * n
        min_heap = []
        
        for i in range(n):
            char = s[i]
            if char == '*':
                if min_heap:
                   
                    _, original_idx_to_delete = heapq.heappop(min_heap)
                    stack[-original_idx_to_delete] = True
            else:
                heapq.heappush(min_heap, (char, -i))
        
        result_chars = []
        for i in range(n):
            if s[i] != '*' and not stack[i]:
                result_chars.append(s[i])
                
        return "".join(result_chars)

print(Solution().clearStars(s = "aaba*"))
print(Solution().clearStars(s = "abc"))