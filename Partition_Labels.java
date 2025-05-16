/* 
763. Partition Labels
Medium
Topics
Companies
Hint
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters. */
import java.util.*;

public class Partition_Labels {
    // Approach: Greedy
    public List<Integer> partitionLabels(String s) {
        int n = s.length();
        int[] lastIndex = new int[26];
        for (int i = 0; i < n; i++) {
            lastIndex[s.charAt(i) - 'a'] = i;
        }
        List<Integer> result = new ArrayList<>();
        int start = 0;
        int end = 0;
        for (int i = 0; i < n; i++) {
            end = Math.max(end, lastIndex[s.charAt(i) - 'a']);
            if (i == end) {
                result.add(end - start + 1);
                start = end + 1;
            }
        }
        return result;

    }
    public static void main(String[] args) {
        Partition_Labels partitionLabels = new Partition_Labels();
        String s = "ababcbacadefegdehijhklij";
        List<Integer> result = partitionLabels.partitionLabels(s);
        System.out.println(result);
        String s2 = "eccbbbbdec";
        List<Integer> result2 = partitionLabels.partitionLabels(s2);
        System.out.println(result2);
    }
}