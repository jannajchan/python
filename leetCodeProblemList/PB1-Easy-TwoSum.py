"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 1: Two Sum
# https://leetcode.com/problems/two-sum/
# ----------------------------------------------------------------------------------------------------------------------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

>Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

>Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

>Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
>Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
# ----------------------------------------------------------------------------------------------------------------------
"""

from typing import List

class Solution:
    # Approach 1: Brute Force
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []
    
    # Approach 2: Two-pass Hash Table
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        # If no valid pair is found, return an empty list
        return []

    # Approach 3: One-pass Hash Table
    def twoSum_3(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []

solution = Solution()
print("Ex1:", solution.twoSum_3([2,7,11,15], 9))    # Output: [0, 1]
print("Ex2:", solution.twoSum_3([3,2,4], 6))        # Output: [1, 2]
print("Ex3:", solution.twoSum_3([3,3], 6))          # Output: [0, 1]