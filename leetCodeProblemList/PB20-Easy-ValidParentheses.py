"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 20: Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# ----------------------------------------------------------------------------------------------------------------------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 
>Example 1:
Input: s = "()"
Output: true

>Example 2:
Input: s = "()[]{}"
Output: true

>Example 3:
Input: s = "(]"
Output: false

>Example 4:
Input: s = "([])"
Output: true

>Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
# ----------------------------------------------------------------------------------------------------------------------
"""

import re

class Solution:
    def isValid(self, s: str) -> bool:
        if not s or not re.fullmatch("[\(\)\[\]\{\}]*", s): # Check if the string is empty or contains invalid characters
            return False
        else:
            stack = []
            opening_brackets_mapping = {"(": ")", "{": "}", "[": "]"}

            for char in s:
                if char in opening_brackets_mapping:
                    stack.append(char)
                # --------------------------------------------
                # | if not stack => check if stack is empty  |
                # | if stack     => check if stack has value |
                # --------------------------------------------
                # Make sure that stack has value, then check if the last opened bracket matches the current closing bracket
                elif not stack or char != opening_brackets_mapping[stack.pop()]:
                    return False
                        
            return not stack

solution = Solution()
print("Ex1:", solution.isValid("()"))       # True
print("Ex2:", solution.isValid("()[]{}"))   # True
print("Ex3:", solution.isValid("(]"))       # False
print("Ex4:", solution.isValid("([])"))     # True
print("Ex5:", solution.isValid("([x])"))    # False
print("Ex6:", solution.isValid(""))         # False
print("Ex7:", solution.isValid("]"))        # False
print("Ex8:", solution.isValid("([)]"))     # False