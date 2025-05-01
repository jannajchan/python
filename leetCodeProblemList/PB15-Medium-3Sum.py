"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 15: 3 Sum
# https://leetcode.com/problems/3sum/
# ----------------------------------------------------------------------------------------------------------------------
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

>Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

>Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

>Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
>Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
# ----------------------------------------------------------------------------------------------------------------------
"""

from bisect import bisect_left, bisect_right
from typing import List
from collections import Counter, defaultdict
from itertools import islice, takewhile

class Solution:
    # Approach 1: Sorting + Two Pointers
    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort the input list to make it easier to avoid duplicates.
        result = []

        # Use "len(nums) - 2" because we need 3 numbers, so we don’t go out of bounds.
        for i in range(len(nums) - 2):
            
            # To avoids repeating the same starting number at index i.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Fix one number and use two pointers to find two other numbers that sum with nums[i], add up to 0.
            # The left pointer starts just after i, and the right pointer starts at the end of the list.
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    # Found triplet that sums to 0, add the triplet to the result list.
                    result.append([nums[i], nums[left], nums[right]])

                    # To skip duplicates: (1) Move the left pointer to the right (2) Move the right pointer to the left.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers to continue searching the next result numbers.
                    left += 1
                    right -= 1
                
                # If the sum is less than 0, we need a larger number, so move the left pointer to right.
                elif s < 0:
                    left += 1
                
                # If the sum is greater than 0, we need a smaller number, so move the right pointer to left.
                else:
                    right -= 1
        
        return result
    
    # Approach 2: Hash Map + Two Pointers
    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        negative = defaultdict(int)
        positive = defaultdict(int)
        zeros = 0
        for num in nums:
            if num < 0:
                negative[num] += 1
            elif num > 0:
                positive[num] += 1
            else:
                zeros += 1
        
        result = []
        if zeros:
            for n in negative:
                if -n in positive:
                    result.append((0, n, -n))       
            if zeros > 2:
                result.append((0,0,0))

        for set1, set2 in ((negative, positive), (positive, negative)):
            set1Items = list(set1.items())
            for i, (j, k) in enumerate(set1Items):
                for j2, k2 in set1Items[i:]:
                    if j != j2 or (j == j2 and k > 1):
                        if -j-j2 in set2:
                            result.append((j, j2, -j-j2))
        return result
    
    # Approach 3: Optimized Hash Map + Two Pointers (Binary Search)
    # https://leetcode.com/problems/3sum/solutions/3523898/beats-99-48-44-145-top-interview-question/
    def threeSum_3(self, nums: List[int]) -> List[List[int]]: #👏😎
        setN = Counter(nums)
        ans = [(0, 0 ,0)] if setN.get(0, -1) > 2 else []
        nums = sorted(setN)
        if not nums or nums[0] > 0 or nums[-1] < 0:
            return ans

        del setN[0]
        for n in nums:
            if n%2 == 0 and setN[-n//2] > 1:
                ans.append((-n//2, -n//2, n))
        
        setN = set(-i for i in takewhile(lambda n: n > 0, reversed(nums)))
        maxN = nums[-1]
        for i, a in takewhile(lambda n: n[1] < 0, enumerate(nums)):
            left = bisect_left(nums, -a-maxN, lo= i+1)
            right = bisect_right(nums, (-a-1)//2, lo= left)
            for b in islice(nums, left, right):
                if a+b in setN:
                    ans.append((a, b, -a-b))
        return ans

solution = Solution()
print("Ex1:", solution.threeSum_3([-1,0,1,2,-1,-4]))    # Output: [(-1, -1, 2), (-1, 0, 1)]
print("Ex2:", solution.threeSum_3([0,1,1]))             # Output: []
print("Ex3:", solution.threeSum_3([0,0,0]))             # Output: [(0, 0, 0)]