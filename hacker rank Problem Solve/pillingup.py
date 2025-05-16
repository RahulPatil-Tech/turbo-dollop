'''
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example

Result: No

After choosing the rightmost element, , choose the leftmost element, . After than, the choices are  and . These are both larger than the top block of size .


Result: Yes

Choose blocks from right to left in order to successfully stack the blocks.

Input Format

The first line contains a single integer , the number of test cases.
For each test case, there are  lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Constraints




Output Format

For each test case, output a single line containing either Yes or No.

Sample Input

STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]
Sample Output

Yes
No
Explanation

In the first test case, pick in this order: left - , right - , left - , right - , left - , right - .
In the second test case, no order gives an appropriate arrangement of vertical cubes.  will always come after either  or .
'''
'''
Approach:
Understanding the process:

We can only take cubes from the leftmost or the rightmost positions at each step.
To form a valid stack, we need to ensure that the cube on top is smaller than the one below.
This means we have to continuously check if we can pick cubes from either end while maintaining this rule.
Strategy:

Use two pointers: one at the leftmost (left) and one at the rightmost (right) ends of the sequence of cubes.
Compare the cubes at these two positions.
Always pick the cube that is smaller and reduce the available set of cubes from either the left or the right.
If at any point, neither of the cubes (leftmost or rightmost) can be placed on top of the current cube (i.e., both are larger), then it's not possible to form a valid stack.
Steps:

For each test case, initialize two pointers at both ends of the list of cubes.
Try to simulate the stacking process by picking the smaller of the two cubes from the ends until all cubes are used or a valid stack cannot be formed.
If we successfully stack all cubes, print "Yes", otherwise print "No".
Solution Implementation:
'''
def can_stack_cubes(blocks):
    left = 0
    right = len(blocks) - 1
    current = float('inf')  # The size of the cube that should be placed on top of the pile
    
    while left <= right:
        # Check if we can pick the leftmost cube
        if blocks[left] <= current and (blocks[left] >= blocks[right] or blocks[right] > current):
            current = blocks[left]
            left += 1
        # Check if we can pick the rightmost cube
        elif blocks[right] <= current:
            current = blocks[right]
            right -= 1
        else:
            return "No"
    
    return "Yes"

def main():
    T = int(input())  # Number of test cases
    for _ in range(T):
        n = int(input())  # Number of cubes in this test case
        blocks = list(map(int, input().split()))  # Cube sizes
        print(can_stack_cubes(blocks))

if __name__ == "__main__":
    main()
