'''
21. Merge Two Sorted Lists
Solved
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return 

        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        
        return dummy.next
    
    # Helper function to create a linked list from a list
    def create_linked_list(self, arr):
        dummy = ListNode()
        current = dummy
        for value in arr:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    # Helper function to print a linked list
    def print_linked_list(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        print(result)

# Example inputs
solution = Solution()
list1 = solution.create_linked_list([1, 2, 4])
list2 = solution.create_linked_list([1, 3, 4])

# Merge lists and print result
merged_list = solution.mergeTwoLists(list1, list2)
solution.print_linked_list(merged_list)  # Output: [1, 1, 2, 3, 4, 4]