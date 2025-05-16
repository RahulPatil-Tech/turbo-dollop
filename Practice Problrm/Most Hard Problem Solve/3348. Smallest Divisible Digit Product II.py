'''
3348. Smallest Divisible Digit Product II
Hard
Topics
Companies
Hint
You are given a string num which represents a positive integer, and an integer t.

A number is called zero-free if none of its digits are 0.

Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".

 

Example 1:

Input: num = "1234", t = 256

Output: "1488"

Explanation:

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

Example 2:

Input: num = "12355", t = 50

Output: "12355"

Explanation:

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

Example 3:

Input: num = "11111", t = 26

Output: "-1"

Explanation:

No number greater than 11111 has the product of its digits divisible by 26.

 

Constraints:

2 <= num.length <= 2 * 105
num consists only of digits in the range ['0', '9'].
num does not contain leading zeros.
1 <= t <= 1014
'''
# Solution 
from math import prod
from collections import Counter
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        c = Counter()
        for p in [2, 3, 5, 7]:
            while not t % p:
                c[p] += 1
                t //= p
        if t != 1:
            return '-1'
        
        def min_req(c):
            eight, mod = divmod(c[2], 3)
            nine, three = divmod(c[3], 2)
            if not mod:
                two = four = 0
            elif mod == 1:
                two, four = 1, 0
            else:
                two, four = 0, 1
            if two and three:
                six = 1
                two = three = 0
            else:
                six = 0
            if three and four:
                two = six = 1
                three = four = 0
            return (two, three, four, c[5], six, c[7], eight, nine)
        
        code = ['2', '3', '4', '5', '6', '7', '8', '9']
        req = min_req(c)
        if sum(req) > len(num):
            return ''.join(d * x for d, x in zip(code, req))
        
        factors = [Counter(),
                   Counter(),
                   Counter([2]),
                   Counter([3]),
                   Counter([2, 2]),
                   Counter([5]),
                   Counter([2, 3]),
                   Counter([7]),
                   Counter([2, 2, 2]),
                   Counter([3, 3])]
        
        total = sum((factors[int(d)] for d in num), start = Counter())
        first_zero = n = len(num)
        for i, d in enumerate(num):
            if d == '0':
                first_zero = i
                break
        if first_zero == n:
            if not c - total:
                return num
        
        for i in reversed(range(n)):
            d = int(num[i])
            total -= factors[d]
            space = n - i - 1
            if i <= first_zero:
                for option in range(d + 1, 10):
                    req = min_req(c - (total + factors[option]))
                    if sum(req) <= space:
                        ones = space - sum(req)
                        return num[:i] + str(option) + '1' * ones + ''.join(d * x for d, x in zip(code, req))
        req = min_req(c)
        return '1' * (n + 1 - sum(req)) + ''.join(d * x for d, x in zip(code, req))
print(Solution().smallestNumber(num = "1234", t = 256))
print(Solution().smallestNumber(num = "12355", t = 50))
print(Solution().smallestNumber(num = "11111", t = 26))