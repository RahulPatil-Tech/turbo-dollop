'''
22. Generate Parentheses
Attempted
Medium
Topics
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 0
'''
# Solution 
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def genrate(open , close, curr):
            if open + close == 2*n:
                res.append(curr)
                return
            
            if open < n:
                genrate(open+1, close, curr + '(')
            
            if close < open:
                genrate(open, close + 1, curr + ')')
        
        genrate(0, 0, '')
        return res
        
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_count: int, close_count: int, current: str) -> List[str]:
            # Base case: if the current string has 2n characters, return it as a list
            if len(current) == 2 * n:
                return [current]
            
            # Use list comprehension to build the result
            return (
                backtrack(open_count + 1, close_count, current + '(') if open_count < n else []
            ) + (
                backtrack(open_count, close_count + 1, current + ')') if close_count < open_count else []
            )
        
        # Start the backtracking process with 0 open and close parentheses
        return backtrack(0, 0, '')
'''