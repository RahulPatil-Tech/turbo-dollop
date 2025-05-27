'''
2131. Longest Palindrome by Concatenating Two Letter Words
Medium
Topics
Companies
Hint
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
'''
# Solution ():
from collections import Counter
from collections import Counter

class Solution:
    def longestPalindrome(self, words):
        w_c = Counter(words)
        l = 0
        uc = False

        for word in w_c:
            reversed_word = word[::-1]
            if word != reversed_word:
                if reversed_word in w_c:
                    pairs = min(w_c[word], w_c[reversed_word])
                    l += pairs * 4
                    w_c[word] -= pairs
                    w_c[reversed_word] -= pairs
            else:
                pairs = w_c[word] // 2
                l += pairs * 4
                w_c[word] -= pairs * 2
                if not uc and w_c[word] > 0:
                    l += 2
                    uc = True

        return l



# Test cases
print(Solution().longestPalindrome(words = ["lc","cl","gg"]))  # type: ignore # Output: 6
print(Solution().longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"]))  # type: ignore # Output
print(Solution().longestPalindrome(words =["cc", "ll", "xx"]))  # type: ignore # Output: 2
print(Solution().longestPalindrome(words =["a", "a"]))  # type: ignore # Output: 2
