"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 69: Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# ----------------------------------------------------------------------------------------------------------------------
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
- For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

>Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

>Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
>Constraints:
0 <= x <= 231 - 1
# ----------------------------------------------------------------------------------------------------------------------
"""

class Solution:
    def mySqrt_linear_search(self, x: int) -> int: # Brute Force
        i = 0
        while i * i <= x:
            i += 1
        return i - 1

    def mySqrt_binary_search(self, x: int) -> int:
        low = 0
        high = x
        while (low <= high):
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else: # mid * mid > x
                high = mid - 1
        return high
    
    def mySqrt_newton_method(self, x: int) -> int: #👏😎
        guess = x
        while guess * guess > x:
            guess = (guess + x // guess) // 2
        return guess

solution = Solution()
print("Ex1:", solution.mySqrt_newton_method(4))         # Output: 2
print("Ex2:", solution.mySqrt_newton_method(8))         # Output: 2     # sqrt(8) ≈ 2.828, but return floor 2
print("Ex3:", solution.mySqrt_newton_method(81))        # Output: 9
print("Ex4:", solution.mySqrt_newton_method(22500))     # Output: 150
print("Ex4:", solution.mySqrt_newton_method(10))        # Output: 3
