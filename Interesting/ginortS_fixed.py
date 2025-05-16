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
# Solution ; binary search
def ginortS(s):
    def sort_key(x):
        if x.islower():
            return (0, x)
        elif x.isupper():
            return (1, x)
        elif x.isdigit():
            # Odd digits first
            if int(x) % 2 == 1:
                return (2, x)
            else:
                return (3, x)
    return ''.join(sorted(s, key=sort_key))

# Example usage
print(ginortS("Sorting1234"))  # Expected output: ginortS1324
