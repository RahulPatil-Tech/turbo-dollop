'''
23. Merge k Sorted Lists
Hard
Topics
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''
# Solution 
from heapq import heappop, heappush, heapify
from typing import List, Optional
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution():
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapify(heap)
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, idx, node = heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(heap, (node.next.val, idx, node.next))
                
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
lists = [[1,4,5], [1,3,4], [2,6]]
linked_lists = [list_to_linkedlist(lst) for lst in lists]
merged = Solution().mergeKLists(linked_lists)
print(linkedlist_to_list(merged))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]

lists = []
linked_lists = [list_to_linkedlist(lst) for lst in lists]
merged = Solution().mergeKLists(linked_lists)
print(linkedlist_to_list(merged))  # Output: []
