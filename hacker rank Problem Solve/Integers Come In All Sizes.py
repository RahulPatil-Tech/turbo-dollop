'''
Integers Come In All Sizes
51/115 challenges solved
Rank: 55673|Points: 1095
Python
Problem
Submissions
Leaderboard
Discussions
Editorial
Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  (c++ int) or  (C++ long long int).

As we know, the result of  grows really fast with increasing .

Let's do some calculations on very large integers.

Task
Read four numbers, , , , and , and print the result of .

Input Format
Integers , , , and  are given on four separate lines, respectively.

Constraints




Output Format
Print the result of  on one line.

Sample Input

9
29
7
27
Sample Output

4710194409608608369201743232  
Note: This result is bigger than . Hence, it won't fit in the long long int of C++ or a 64-bit integer.
'''
# Read four integers from input
a = int(input("Enter First Number: "))  
b = int(input("Enter Second Number: "))  
c = int(input("Enter Third Number: "))  
d = int(input("Enter Forth Number: "))  

# Compute the result of (a^b) + (c^d)
result = (pow(a, b) + pow(c, d))
print(result)