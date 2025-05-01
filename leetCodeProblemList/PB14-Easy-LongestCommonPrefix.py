"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 14: Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# ----------------------------------------------------------------------------------------------------------------------
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

>Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

>Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
>Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
# ----------------------------------------------------------------------------------------------------------------------
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        if len(strs) == 0: # Check if the list is empty
            return prefix
        else:
            sorted_strs = sorted(strs, key=len)
            for i in range(len(sorted_strs[0])):
                for j in range(1, len(sorted_strs)):
                    if sorted_strs[j][i] != sorted_strs[0][i]:
                        return prefix
                prefix += sorted_strs[0][i]

        return prefix

solution = Solution()
print("Ex1:", solution.longestCommonPrefix(["flower","flow","flight"])) # Output: "fl"
print("Ex2:", solution.longestCommonPrefix(["dog","racecar","car"]))    # Output: ""
print("Ex3:", solution.longestCommonPrefix([]))                         # Output: ""
print("Ex4:", solution.longestCommonPrefix(["disagree","discharge","discontinue","dis-washing","dispatch","disturb"]))  # Output: "dis"