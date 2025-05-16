'''
24. Swap Nodes in Pairs
Medium
Topics
Companies
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

'''
'''
1. Initialize a dummy node and point it to the head of the list.
2. Set `current` to the dummy node.
3. While `current.next` and `current.next.next` exist:
    a. Identify the two nodes to be swapped: `first` and `second`.
    b. Perform the swap:
        i. `first.next = second.next`
        ii. `second.next = first`
        iii. `current.next = second`
    c. Move `current` two steps forward.
4. Return the new head (dummy.next).

'''
# Solution 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            first, second = current.next, current.next.next
            
            first.next = second.next
            second.next = first 
            current.next = second
            
            current = first
        return dummy.next
'''

from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first_node, second_node = head, head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        return second_node
    
# Creating a linked list [1, 2, 3, 4]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# Create an instance of the Solution class
solution = Solution()

# Swapping nodes in pairs
result = solution.swapPairs(head)

# Helper function to convert linked list to Python list using list comprehension
def linked_list_to_list(node):
    return [node.val for node in iter_linked_list(node)]

# Helper generator function to iterate through the linked list
def iter_linked_list(node):
    while node:
        yield node
        node = node.next

print(linked_list_to_list(result))  # Output: [2, 1, 4, 3]