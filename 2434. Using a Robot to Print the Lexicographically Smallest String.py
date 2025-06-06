'''
2434. Using a Robot to Print the Lexicographically Smallest String
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.

 

Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
Example 2:

Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".
Example 3:

Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".
 

Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.'''
# Solution():  Hashtable, greedy 
class Solution():
    def robotWithString(self, s: str) -> str:
        n = len(s)
        s_min = [''] * n
        s_min[n - 1] = s[n-1]
        for i in range(n - 2, -1, -1):
            s_min[i] = min(s_min[i + 1], s[i])
        t = []
        ans = []
        for i in range(n):
            t.append(s[i])
            c_s_min = s_min[i +1] if (i + 1) < n else '{'
            while t and t[-1] <= c_s_min:
                ans.append(t.pop())
        while t:
            ans.append(t.pop())

        return "".join(ans)
print(Solution().robotWithString(s = "zza"))
print(Solution().robotWithString(s = "bac"))
print(Solution().robotWithString(s = "bdda"))