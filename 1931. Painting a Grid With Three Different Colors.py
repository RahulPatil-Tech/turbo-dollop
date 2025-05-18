'''
1931. Painting a Grid With Three Different Colors
Hard
Topics
Companies
Hint
You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.
Example 2:


Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.
Example 3:

Input: m = 5, n = 5
Output: 580986
 

Constraints:

1 <= m <= 5
1 <= n <= 1000
'''
# Appraoch:  Dynamic Programming with Matrix Exponentiation.
import collections
class Solution:
    def painting_grid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        def get_valid_configs(row_index, current_config):
            if row_index == m:
                return [tuple(current_config)]

            valid_configs = []
            for color in range(3):
                if not current_config or current_config[-1] != color:
                    valid_configs.extend(get_valid_configs(row_index + 1, current_config + [color]))
            return valid_configs

        valid_configs = get_valid_configs(0, [])
        num_configs = len(valid_configs)
        config_to_index = {config: i for i, config in enumerate(valid_configs)}

        transition_matrix = [[0] * num_configs for _ in range(num_configs)]

        for i in range(num_configs):
            for j in range(num_configs):
                config1 = valid_configs[i]
                config2 = valid_configs[j]
                valid_transition = True
                for k in range(m):
                    if config1[k] == config2[k]:
                        valid_transition = False
                        break
                if valid_transition:
                    transition_matrix[i][j] = 1

        def multiply_matrices(A, B):
            rows_A = len(A)
            cols_A = len(A[0])
            rows_B = len(B)
            cols_B = len(B[0])
            if cols_A != rows_B:
                raise ValueError("Matrices can't be multiplied!")
            C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
            for i in range(rows_A):
                for j in range(cols_B):
                    for k in range(cols_A):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def power(matrix, exp):
            size = len(matrix)
            result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
            while exp > 0:
                if exp % 2 == 1:
                    result = multiply_matrices(result, matrix)
                matrix = multiply_matrices(matrix, matrix)
                exp //= 2
            return result

        if n == 1:
            return num_configs

        result_matrix = power(transition_matrix, n - 1)

        initial_vector = [1] * num_configs
        final_vector = [0] * num_configs

        for i in range(num_configs):
            for j in range(num_configs):
                final_vector[i] = (final_vector[i] + result_matrix[j][i] * initial_vector[j]) % MOD

        return sum(final_vector) % MOD
    
print(Solution().painting_grid(m = 1, n = 1))
print(Solution().painting_grid(m = 1, n = 2))
print(Solution().painting_grid(m = 5, n = 5))