'''

2929. Distribute Candies Among Children II
Medium
Topics
premium lock icon
Companies
Hint
You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

 

Example 1:

Input: n = 5, limit = 2
Output: 3
Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
Example 2:

Input: n = 3, limit = 3
Output: 10
Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).
 

Constraints:

1 <= n <= 106
1 <= limit <= 106'''
# Solution(): Math Combinatorics Enumeration

import time
class Solution(object):
    def distributeCandies(self, n, limit):
        l = 0
        for i in range(min(limit, n) + 1):
            if n - i > 2 * limit:
                continue
            l += min(n - i, limit) - max(0, n - i - limit) + 1
        return l
    
class Solution1(object):
    def combinations(self, n, k):
        """
        Calculates nCk (n choose k).
        Returns 0 if k is out of bounds (k < 0 or k > n).
        """
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        if k > n // 2:  # Use symmetry C(n, k) = C(n, n-k) to reduce calculations
            k = n - k
        
        res = 1
        for i in range(k):
            res = res * (n - i) // (i + 1)
        return res

    def distributeCandies(self, n, limit):
        """
        Calculates the number of ways to distribute 'n' identical candies to 3 children,
        such that each child receives at most 'limit' candies.
        Uses the inclusion-exclusion principle.
        """

        # Helper function to calculate the number of non-negative integer solutions
        # to x1 + x2 + x3 = target_n, using stars and bars: C(target_n + k - 1, k - 1)
        # For k=3 children, this is C(target_n + 2, 2)
        def count_non_negative_solutions(target_n):
            if target_n < 0:
                return 0
            return self.combinations(target_n + 2, 2)

        # 1. Total number of ways to distribute 'n' candies to 3 children
        # without any upper limit (each child can receive any non-negative amount).
        # This is equivalent to solutions for c1 + c2 + c3 = n.
        total_ways = count_non_negative_solutions(n)

        # 2. Subtract cases where at least one child exceeds the limit.
        # Consider a child receiving (limit + 1) candies. The remaining candies are
        # n - (limit + 1). We choose 1 child out of 3.
        # Formula: C(3, 1) * count_non_negative_solutions(n - (limit + 1))
        term_one_exceeds = 3 * count_non_negative_solutions(n - (limit + 1))

        # 3. Add back cases where at least two children exceed the limit.
        # We might have double-subtracted these cases in step 2.
        # Consider two children each receiving (limit + 1) candies. Remaining are
        # n - 2*(limit + 1). We choose 2 children out of 3.
        # Formula: C(3, 2) * count_non_negative_solutions(n - 2 * (limit + 1))
        term_two_exceeds = 3 * count_non_negative_solutions(n - 2 * (limit + 1))

        # 4. Subtract cases where all three children exceed the limit.
        # These cases were added back too many times in step 3.
        # Consider all three children receiving (limit + 1) candies. Remaining are
        # n - 3*(limit + 1). We choose 3 children out of 3.
        # Formula: C(3, 3) * count_non_negative_solutions(n - 3 * (limit + 1))
        term_three_exceeds = 1 * count_non_negative_solutions(n - 3 * (limit + 1))
        
        # Apply the inclusion-exclusion principle:
        # Result = (Total Ways) - (Cases where 1 child exceeds) + (Cases where 2 children exceed) - (Cases where 3 children exceed)
        result = total_ways - term_one_exceeds + term_two_exceeds - term_three_exceeds
        
        return result
start_time = time.time()
print(Solution().distributeCandies(n = 5, limit = 2))
print(Solution().distributeCandies(n = 3, limit = 3))
end_time = time.time()
print("time: ", end_time - start_time, " sec") 
start_time1 = time.time()
print(Solution1().distributeCandies(n = 5, limit = 2))
print(Solution1().distributeCandies(n = 3, limit = 3))
end_time1 = time.time()
print("time: ", end_time1 - start_time1, " sec") 