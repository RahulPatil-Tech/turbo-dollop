class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, second = 0, 0
        while n > 0:
            x = n % 10
            if x > first:
                first, second = x, first
            elif x > second:
                second = x
            n //= 10
        return first * second
print(Solution().maxProduct(31))
print(Solution().maxProduct(22))
print(Solution().maxProduct(124))
