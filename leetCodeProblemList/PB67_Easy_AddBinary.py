"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 67: Add Binary
# https://leetcode.com/problems/add-binary/
# ----------------------------------------------------------------------------------------------------------------------
Given two binary strings a and b, return their sum as a binary string.

>Example 1:
Input: a = "11", b = "1"
Output: "100"

>Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
>Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
# ----------------------------------------------------------------------------------------------------------------------
"""

from typing import List
import numpy as np

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))[2:])
    # -------------------------------------------------------------------
    # | 👆 Explanation: 👆                                             |
    # -------------------------------------------------------------------
    # | If you want to convert string (binary) to integer (decimal),    |
    # |     Ex: a = "1010"          # binary for 10                     |
    # |         b = "1101"          # binary for 13                     |
    # | 1. Using int() with base 2                                      |
    # |         int_a = int(a, 2)                                       |
    # |         int_b = int(b, 2)                                       |
    # | 2. Manual Conversion with a Loop (for learning)                 |
    # |         decimal = 0                                             |
    # |         for i, bit in enumerate(reversed(a)):                   |
    # |             decimal += int(bit) * (2 ** i)                      |
    # |         print(decimal)      # Output: 10                        |
    # | Explanation:                                                    |
    # |     Rightmost bit = least significant bit.                      |
    # |     Multiply each bit by 2ⁱ based on its position.              |
    # -------------------------------------------------------------------
    # | Binary Addition                                                 |
    # |     sum_bin = bin(int_a + int_b)[2:]                            |
    # -------------------------------------------------------------------

solution = Solution()
print("Ex1:", solution.addBinary("11", "1"))        # Output: "100"
print("Ex2:", solution.addBinary("1010", "1011"))   # Output: "10101"