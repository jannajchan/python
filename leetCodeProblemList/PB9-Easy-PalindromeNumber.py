"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 9: Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# ----------------------------------------------------------------------------------------------------------------------
Given an integer x, return true if x is a palindrome, and false otherwise.

>Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

>Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

>Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:
-231 <= x <= 231 - 1
# ----------------------------------------------------------------------------------------------------------------------
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        o = x
        r = 0
        while x > 0:
            t = x % 10
            r = r * 10 + t
            x = x // 10
        
        if r == o: # Check if the reversed number is equal to the original number
            return True
        else:
            return False

solution = Solution()
print("Ex1:", solution.isPalindrome(121))       # Output: True
print("Ex2:", solution.isPalindrome(-121))      # Output: False
print("Ex3:", solution.isPalindrome(10))        # Output: False
print("Ex4:", solution.isPalindrome(12321))     # Output: True
print("Ex5:", solution.isPalindrome(456654))    # Output: True
print("Ex6:", solution.isPalindrome(12345))     # Output: False
print("Ex7:", solution.isPalindrome(-787))      # Output: False