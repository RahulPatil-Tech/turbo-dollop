'''
25. Reverse Nodes in k-Group
Hard
Topics
Companies
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
'''
#Solution
from typing import Optional
from collections import deque 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution():
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev, curr = None, head
            while k >0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev, curr
        
        dummy = ListNode(0)
        dummy.next = head
        prev_grouped_end = dummy
        
        while True:
            # Check if there are at least k nodes remaining
            temp = prev_grouped_end.next
            count = 0
            while temp and count < k:
                temp = temp.next
                count += 1
            
            # If there are fewer than k nodes remaining, no reversal
            if count < k:
                break
            
            # Reverse the current group of k nodes
            group_start = prev_grouped_end.next
            new_group_start, next_group_start = reverse(group_start, k)
            
            # Connect reversed group
            prev_grouped_end.next = new_group_start
            group_start.next = next_group_start
            
            # Move `prev_grouped_end` to the end of the reversed group
            prev_grouped_end = group_start
        
        return dummy.next
 # Utility: Convert a list to a linked list
def list_to_linkedlist(arr):
    if not arr:
        return None
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Utility: Convert a linked list to a Python list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage
solution = Solution()

# Test case 1
head = list_to_linkedlist([1, 2, 3, 4, 5])
k = 2
result = solution.reverseKGroup(head, k)
print(linkedlist_to_list(result))  # Output: [2, 1, 4, 3, 5]

# Test case 2
head = list_to_linkedlist([1, 2, 3, 4, 5])
k = 3
result = solution.reverseKGroup(head, k)
print(linkedlist_to_list(result))  # Output: [3, 2, 1, 4, 5]