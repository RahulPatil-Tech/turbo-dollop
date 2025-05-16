// 368. Largest Divisible Subset
    // Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
    // Si % Sj = 0 or Sj % Si = 0.
    // If there are multiple solutions, return any of them.
    // Example 1:
    // Input: nums = [1,2,3]
    // Output: [1,2] (or [1,3])
    // Example 2:
    // Input: nums = [1,2,4,8]
    // Output: [1,2,4,8]

    // Approach: Dynamic Programming
    // 1. Sort the input array.
    // 2. Create a dp array where dp[i] represents the size of the largest divisible subset ending at index i.
    // 3. Create a prev array to keep track of the previous index in the subset.
    // 4. Iterate through the sorted array and update the dp and prev arrays.
    // 5. Find the maximum size in the dp array and backtrack using the prev array to construct the result.
import java.util.*;
 
class Largest_Divisible_Subset {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int[] dp = new int[n];
        int[] prev = new int[n];
        Arrays.fill(dp, 1);
        Arrays.fill(prev, -1);
        int maxSize = 1;
        int maxIndex = 0;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0 && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
            if (dp[i] > maxSize) {
                maxSize = dp[i];
                maxIndex = i;
            }
        }
        List<Integer> result = new ArrayList<>();
        while (maxIndex != -1) {
            result.add(nums[maxIndex]);
            maxIndex = prev[maxIndex];
        }
        Collections.reverse(result);
        return result;
    }
    public static void main(String[] args) {
        Largest_Divisible_Subset solution = new Largest_Divisible_Subset();
        int[] nums = {1, 2, 3};
        List<Integer> result = solution.largestDivisibleSubset(nums);
        System.out.println(result); // Output: [1, 2] or [1, 3]
        int[] nums2 = {1, 2, 4, 8};
        List<Integer> result2 = solution.largestDivisibleSubset(nums2);
        System.out.println(result2); // Output: [1, 2, 4, 8]
        }
    }
    // Time Complexity: O(n^2) where n is the number of elements in th
    // Space Complexity: O(n) for the dp and prev arrays
    // The algorithm uses dynamic programming to find the largest divisible subset.
    // It sorts the input array and then iterates through it, updating the dp array
    // to keep track of the size of the largest divisible subset ending at each index.
