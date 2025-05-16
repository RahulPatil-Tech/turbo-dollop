'''
Check Tutorial tab to know how to to solve.

You are given a string  consisting only of digits 0-9, commas ,, and dots .

Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in .

It’s guaranteed that every comma and every dot in  is preceeded and followed by a digit.

Sample Input 0

100,000,000.000
Sample Output 0

100
000
000
000
'''
# Solution
import re

# Read input string
input_string = input().strip()

# Define the regex pattern for splitting by comma or dot
regex_pattern = r'[,.]'

# Split the string based on the regex pattern
result = re.split(regex_pattern, input_string)

# Print each segment on a new line
for segment in result:
    print(segment)
