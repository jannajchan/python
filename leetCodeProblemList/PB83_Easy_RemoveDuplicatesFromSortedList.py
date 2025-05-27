"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 83: Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# ----------------------------------------------------------------------------------------------------------------------
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

>Example 1:
Input: head = [1,1,2]
Output: [1,2]

>Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
 
>Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
# ----------------------------------------------------------------------------------------------------------------------
"""

from typing import Optional

# --- ListNode Class ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --- Helper Functions ---
# To convert Python list to Linked List
def build_linked_list(list):
    if not list:
        return None
    head = ListNode(list[0])
    current = head
    for val in list[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# To print Linked List
def print_linked_list(head: Optional[ListNode]):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# To build Linked List from input list, and call function deleteDuplicates
def deleteDuplicatesLinkedList(list):
    head = build_linked_list(list)
    solution = Solution()
    deleted = solution.deleteDuplicates(head)
    print_linked_list(deleted)

# --- Solution Class ---
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next    # Skip the duplicate node
            else:
                current = current.next
        return head

print("Ex1:", end=" ")
deleteDuplicatesLinkedList([1,1,2])         # Output: 1 -> 2 -> None

print("Ex2:", end=" ")
deleteDuplicatesLinkedList([1,1,2,3,3])     # Output: 1 -> 2 -> 3 -> None