'''
30. Substring with Concatenation of All Words
Hard
Topics
Companies
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
'''
'''
Step 1: Understanding the Problem
Each word in words has the same length.
A concatenated substring consists of all the words in words in any order.
If words = ["foo", "bar"], valid substrings include "foobar" and "barfoo".

Step 2: Key Observations
The total length of the concatenated substring is total_len = len(words) * len(words[0]).
Sliding through s, each substring of length total_len needs to be checked to determine if it’s a valid concatenation of words.

Step 3: Algorithm
1. Initialize Necessary Variables
word_len = len(words[0]): All words have the same length.
total_len = len(words) * word_len: Total length of the concatenated substring.
A word_count dictionary to store the frequency of each word in words.

2. Sliding Window Approach
Traverse the string s in chunks of size word_len.
For each starting index i from 0 to len(s) - total_len:
Extract the substring of length total_len starting at i.
Divide the substring into words of size word_len.
Check if the frequency of words matches word_count.

3. Validate with Frequency Matching
Use a hashmap to count the occurrences of words in the substring.
If the counts match, record the starting index i.

Step 4: Implementing the Solution
'''
#Solution
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        words_length = len(words[0])
        total_length = len(words) * words_length 
        word_count = Counter(words)  # Use Counter for efficient word counting
        
        result = []
        
        for i in range(len(s) - total_length + 1):
            # Extract the substring of length `total_length`
            substring = s[i:i + total_length]
            
            # Split the substring into words of length `words_length`
            substring_words = [
                substring[j:j + words_length]
                for j in range(0, total_length, words_length)
            ]
            
            # Check if the frequency of words in the substring matches `word_count`
            if Counter(substring_words) == word_count:
                result.append(i)
        
        return result