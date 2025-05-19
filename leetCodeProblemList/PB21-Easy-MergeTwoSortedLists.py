"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 21: Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# ----------------------------------------------------------------------------------------------------------------------
You are given the heads of two sorted linked lists, list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

>Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

>Example 2:
Input: list1 = [], list2 = []
Output: []

>Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

>Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
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
    def mergeTwoLists_RecuriveApproach(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: #👏😎
        if not list1 or not list2:
            return list1 or list2
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists_RecuriveApproach(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_RecuriveApproach(list1, list2.next)
            return list2
    
    def mergeTwoLists_IterativeApproach(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 or list2
        return dummy.next

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

# To parse two lists to merge
def parse2ListToMerge(list1, list2):
    list1 = build_linked_list(list1)
    list2 = build_linked_list(list2)

    solution = Solution()
    merged = solution.mergeTwoLists_RecuriveApproach(list1, list2)
    print_linked_list(merged)

print("Ex1:", end=" ")
parse2ListToMerge([1,2,4], [1,3,4])         # Output: [1, 1, 2, 3, 4, 4]                1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None

print("Ex2:", end=" ")
parse2ListToMerge([], [])                   # Output: []                                None

print("Ex3:", end=" ")
parse2ListToMerge([], [0])                  # Output: [0]                               0 -> None

print("Ex4:", end=" ")
parse2ListToMerge([0], [])                  # Output: [0]                               0 -> None

print("Ex5:", end=" ")
parse2ListToMerge([1,3,5,7,9], [2,6,8,9])   # Output: [1, 2, 3, 5, 6, 7, 8, 9, 9]       1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 9 -> 9 -> None