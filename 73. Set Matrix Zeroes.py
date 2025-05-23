'''
73. Set Matrix Zeroes
Medium
Topics
Companies
Hint
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?'''
# Solution(): hash table and matrix
from collections import defaultdict
import time
class Solution():
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        row = defaultdict(bool)
        col = defaultdict(bool)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        return matrix
start_time = time.time()
print(Solution().setZeroes( matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
print(Solution().setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]]))
end_time = time.time()
expected_time = start_time - end_time // 2
print(f"Expected time: {expected_time}")


# more optimized Solution:
import time

# Assuming your Solution class is defined as provided earlier (the O(1) space version)
class Solution1():
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        for c in range(n):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        for r in range(m):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_has_zero:
            for c in range(n):
                matrix[0][c] = 0

        if first_col_has_zero:
            for r in range(m):
                matrix[r][0] = 0

# --- Test and Timing ---

# Test Case 1
matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
start_time_1 = time.time()
Solution1().setZeroes(matrix1) # Modifies matrix1 in-place
end_time_1 = time.time()
elapsed_time_1 = end_time_1 - start_time_1

print(f"Matrix 1 after setZeroes: {matrix1}")
print(f"Elapsed time for Matrix 1: {elapsed_time_1:.6f} seconds") # Format to 6 decimal places for readability

print("-" * 30) # Separator

# Test Case 2
matrix2 = [[1,1,1],[1,0,1],[1,1,1]]
start_time_2 = time.time()
Solution1().setZeroes(matrix2) # Modifies matrix2 in-place
end_time_2 = time.time()
elapsed_time_2 = end_time_2 - start_time_2

print(f"Matrix 2 after setZeroes: {matrix2}")
print(f"Elapsed time for Matrix 2: {elapsed_time_2:.6f} seconds")

# If you still want a total time for both operations:
total_start_time = time.time()
temp_matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
temp_matrix2 = [[1,1,1],[1,0,1],[1,1,1]]
Solution1().setZeroes(temp_matrix1)
Solution1().setZeroes(temp_matrix2)
total_end_time = time.time()
total_elapsed_time = total_end_time - total_start_time
print("-" * 30)
print(f"Total elapsed time for both operations: {total_elapsed_time:.6f} seconds")