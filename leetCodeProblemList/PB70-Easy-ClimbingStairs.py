"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 70: Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# ----------------------------------------------------------------------------------------------------------------------
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

>Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

>Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
>Constraints:
1 <= n <= 45
# ----------------------------------------------------------------------------------------------------------------------
🔰 My Note: ตัวอย่างนี้ มีวิธีการคิดแบบเดียวกับ Fibonacci Sequence
ถ้าก้าวมาจาก ขั้นที่ n-1 → เราต้องใช้วิธีการขึ้นไปถึงขั้น n-1 มาก่อน แล้วจึงก้าวอีก 1 ขั้น (ก้าว 1 ครั้ง)
ถ้าก้าวมาจาก ขั้นที่ n-2 → เราต้องใช้วิธีการขึ้นไปถึงขั้น n-2 มาก่อน แล้วจึงก้าวอีก 2 ขั้น (ก้าว 1 ครั้ง) ** จะไม่รวมแบบก้าวอีก 2 ครั้ง ทีละ 1 ขั้น เนื่องจากเป็นวิธีที่รวมอยู่ในการก้าวมาจากขั้นที่ n-1 แล้ว
ดังนั้น จำนวนวิธีในการขึ้นไปถึงขั้นที่ n คือ ways(n) = ways(n-1) + ways(n-2)
# ----------------------------------------------------------------------------------------------------------------------
"""

class Solution:    
    def climbStairs_iterative(self, n: int) -> int: #👏😎
        if n == 0 or n == 1:
            return 1

        prev1, prev2 = 1, 1
        for i in range(2, n+1):
            prev1, prev2 = prev2, prev1 + prev2
        return prev2
        #     current = prev1 + prev2
        #     prev2 = prev1
        #     prev1 = current
        # return prev1    # To avoid returning 'current' before it is defined, I've used 'prev1' instead, which holds the same value at the end of the process.

    # ⚠️ Warning: This recursive version is very slow for large n due to recomputing subproblems (exponential time).
    def climbStairs_recursive(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs_recursive(n-1) + self.climbStairs_recursive(n-2)

    # -------------------- Optimized the recursive version using memoization --------------------
    # It doesn’t recompute the same subproblems repeatedly.
    # This will turn your recursive solution from exponential time (O(2ⁿ)) to linear time (O(n)).
    def __init__(self):
        self.memo = {}

    def climbStairs_recursive_optimized(self, n: int) -> int:
        print(self.memo)
        if n <= 1:
            return 1
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs_recursive(n-1) + self.climbStairs_recursive(n-2)
        return self.memo[n]
    # -------------------------------------------------------------------------------------------

solution = Solution()
print("Ex1:", solution.climbStairs_iterative(5))                # Output: 8
print("Ex2:", solution.climbStairs_iterative(6))                # Output: 13
print("Ex3:", solution.climbStairs_iterative(7))                # Output: 21
print("Ex4:", solution.climbStairs_recursive(5))                # Output: 8
print("Ex5:", solution.climbStairs_recursive(6))                # Output: 13
print("Ex6:", solution.climbStairs_recursive(7))                # Output: 21
print("Ex7:", solution.climbStairs_recursive_optimized(13))     # Output: 377
print("Ex8:", solution.climbStairs_recursive_optimized(14))     # Output: 610
print("Ex9:", solution.climbStairs_recursive_optimized(15))     # Output: 987
