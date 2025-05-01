"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 876: Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/
# ----------------------------------------------------------------------------------------------------------------------
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

>Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

>Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
>Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
# ----------------------------------------------------------------------------------------------------------------------
"""

from typing import Optional

# --- ListNode Class ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --- Solution Class ---
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _getListNodeLength(head: Optional[ListNode]) -> int:
            length = 0
            index = head
            while index:
                length += 1
                index = index.next
            return length
        
        length = _getListNodeLength(head)
        middle = head
        for _ in range(length // 2):
            middle = middle.next
        return middle

# --- Helper Functions ---
# To convert Python list to Linked List
def build_linked_list(arr) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    #print_linked_list(head)
    return head

# To print Linked List
def print_linked_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

solution = Solution()

print("Ex1:", end=" ")
input1 = build_linked_list([1,2,3,4,5])
print_linked_list(solution.middleNode(input1))      # Output: [3,4,5]

print("Ex2:", end=" ")
input2 = build_linked_list([1,2,3,4,5,6])
print_linked_list(solution.middleNode(input2))      # Output: [4,5,6]