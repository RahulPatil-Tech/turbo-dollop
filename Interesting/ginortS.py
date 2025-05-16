'''
You are given a string .
 contains alphanumeric characters only.
Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324

'''

# Solution : Binary Search
def ginortS(s):
    # Sort the string using a custom key
    s= list(s)
    sorted_string = sorted(s, key=lambda x: (x.isdigit(), x.isupper(), x.islower(), int(x) % 2))
    return ''.join(sorted_string)
# Example usage
print(ginortS("Sorting1234"))  # Output: ginortS1324