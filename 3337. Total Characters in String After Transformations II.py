'''
3337. Total Characters in String After Transformations II
Hard
Topics
Companies
Hint
You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
Return the length of the resulting string after exactly t transformations.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

Output: 7

Explanation:

First Transformation (t = 1):

'a' becomes 'b' as nums[0] == 1
'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'y' becomes 'z' as nums[24] == 1
'y' becomes 'z' as nums[24] == 1
String after the first transformation: "bcdzz"
Second Transformation (t = 2):

'b' becomes 'c' as nums[1] == 1
'c' becomes 'd' as nums[2] == 1
'd' becomes 'e' as nums[3] == 1
'z' becomes 'ab' as nums[25] == 2
'z' becomes 'ab' as nums[25] == 2
String after the second transformation: "cdeabab"
Final Length of the string: The string is "cdeabab", which has 7 characters.

Example 2:

Input: s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

Output: 8

Explanation:

First Transformation (t = 1):

'a' becomes 'bc' as nums[0] == 2
'z' becomes 'ab' as nums[25] == 2
'b' becomes 'cd' as nums[1] == 2
'k' becomes 'lm' as nums[10] == 2
String after the first transformation: "bcabcdlm"
Final Length of the string: The string is "bcabcdlm", which has 8 characters.

 

Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
1 <= t <= 109
nums.length == 26
1 <= nums[i] <= 25'''
# Solution: Logic: HAshtable String Counting
import time 
class Solution:
    def lengthAfterTransformations(self, s, t, nums):
        MOD = 10**9 + 7
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1

        for _ in range(t):
            new_counts = [0] * 26
            for i in range(26):
                if counts[i] > 0:
                    char = chr(ord('a') + i)
                    transform_len = nums[i]
                    for j in range(transform_len):
                        new_char_ord = (ord(char) - ord('a') + 1 + j) % 26
                        new_counts[new_char_ord] = (new_counts[new_char_ord] + counts[i]) % MOD
            counts = new_counts

        final_length = sum(counts) % MOD
        return final_length
start_time = time.time()
print(Solution().lengthAfterTransformations(s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
print(Solution().lengthAfterTransformations( s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")  # Output:

# Memory Limit Exceed :
'''In short, the error arises from trying to simulate an extremely large number of transformations iteratively, even when working with character counts instead of the full string. This iterative process, while conceptually correct, becomes computationally and memory-intensive for the given constraints.'''
class Solution1:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = 26

        # 1. Initialize Initial Count Vector
        initial_counts = [0] * n
        for char in s:
            initial_counts[ord(char) - ord('a')] += 1

        # 2. Construct the Transformation Matrix (M)
        transformation_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            transform_length = nums[i]
            for k in range(1, transform_length + 1):
                next_index = (i + k) % n
                transformation_matrix[next_index][i] = 1

        # Function for matrix multiplication (A x B) modulo MOD
        def multiply_matrices(A, B):
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        # Function for matrix power (M^p) using binary exponentiation
        def power(matrix, p):
            result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            while p > 0:
                if p % 2 == 1:
                    result = multiply_matrices(result, matrix)
                matrix = multiply_matrices(matrix, matrix)
                p //= 2
            return result

        # 3. Calculate M^t
        final_transformation_matrix = power(transformation_matrix, t)

        # 4. Multiply M^t by the Initial Count Vector
        final_counts = [0] * n
        for i in range(n):
            for j in range(n):
                final_counts[i] = (final_counts[i] + final_transformation_matrix[i][j] * initial_counts[j]) % MOD

        # 5. Calculate the Total Length
        total_length = sum(final_counts) % MOD
        return total_length

start_time = time.time()
print(Solution1().lengthAfterTransformations(s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
print(Solution1().lengthAfterTransformations( s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")  # Output