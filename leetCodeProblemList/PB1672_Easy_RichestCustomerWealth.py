"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 1672: Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/
# ----------------------------------------------------------------------------------------------------------------------
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

>Example 1:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.

>Example 2:
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.

>Example 3:
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17

>Constraints:
m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
# ----------------------------------------------------------------------------------------------------------------------
"""

from collections import defaultdict
from typing import List

class Solution:
    def maximumWealth_1(self, accounts: List[List[int]]) -> int: #👏😎
        mw = defaultdict(list)
        for i in range(0, len(accounts)):
            total = sum(accounts[i])
            mw[total].append(i + 1)
        return max(mw.keys())
    
    def maximumWealth_2(self, accounts: List[List[int]]) -> int:
        mw = {}
        for i in range(0, len(accounts)):
            total = sum(accounts[i])
            mw.setdefault(total, []).append(i + 1)
        return max(mw.keys())
    
    # Function to return the maximum wealth and the list of customers with that wealth
    def maxWealth(self, accounts: List[List[int]]) -> tuple[int, List[int]]:
        mw = defaultdict(list)
        for i, account in enumerate(accounts):
            total = sum(account)
            mw[total].append(i + 1)
        return max(mw.keys()), mw[max(mw.keys())]
    
solution = Solution()
print("Ex1: Max wealth =", solution.maximumWealth_1([[1,2,3],[3,2,1]]))             # Output: 6
print("Ex2: Max wealth =", solution.maximumWealth_1([[1,5],[7,3],[3,5]]))           # Output: 10
print("Ex3: Max wealth =", solution.maximumWealth_1([[2,8,7],[7,1,3],[1,9,5]]))     # Output: 17
print("Ex4: Max wealth =", solution.maxWealth([[1,2,3],[3,2,1]]))                   # Output: (6, [1, 2])
print("Ex5: Max wealth =", solution.maxWealth([[1,5],[7,3],[3,5]]))                 # Output: (10, [2])
print("Ex6: Max wealth =", solution.maxWealth([[2,8,7],[7,1,3],[1,9,5]]))           # Output: (17, [1])