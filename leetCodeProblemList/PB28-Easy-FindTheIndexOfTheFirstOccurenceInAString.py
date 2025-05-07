"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 28: Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# ----------------------------------------------------------------------------------------------------------------------
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

>Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

>Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
>Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
# ----------------------------------------------------------------------------------------------------------------------
💬 Problem Summary: You are given two strings ...
    - haystack: the main text you're searching in
    - needle: the substring you're looking for
    Your task is to return the index where needle first appears in haystack. If it's not found, return -1.

🧠 Hints to Solve It:
    1. Use a loop
        Loop through each index i in haystack where a substring of the same length as needle can start.
    2. Compare substrings
        At each index i, extract haystack[i:i+len(needle)] and compare it to needle.
    3. Early exit
        Return i as soon as you find a match. If you finish the loop without finding a match, return -1.
# ----------------------------------------------------------------------------------------------------------------------
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Step 1: Handle edge case
        if not needle: # To check if needle == "", return 0
            return 0

        # Step 2: Loop through haystack
        # We loop from index 0 to len(haystack) - len(needle) + 1, because we're sliding a window of size len(needle) across haystack to check if any substring matches needle.
        # Why +1? Because we want to include the last possible starting index where needle could fit.
        for i in range(len(haystack) - len(needle) + 1):

            # Step 3: Check if substring matches
            # Inside the loop, we take the substring starting at i with length len(needle) and compare it to needle.
            if haystack[i : i + len(needle)] == needle:
                return i
        
        # Step 4: If loop ends without match, return -1 if needle is not found in any position.
        return -1

solution = Solution()
print("Ex1:", solution.strStr("sadbutsad", "sad"))      # Output: 0
print("Ex2:", solution.strStr("leetcode", "leeto"))     # Output: -1 (No match found)

"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 So Why len(haystack) - len(needle) + 1?
    Because you only want to check up to the last valid window that can fully fit the needle.
        - The last valid start index is:
            len(haystack) - len(needle)
        - And range(...) excludes the end, so to include this last valid index, we use:
            range(len(haystack) - len(needle) + 1)
✅ Summary:
    - It ensures the window doesn't run past the end of the haystack.
    - Prevents out-of-bounds errors.
    - Covers all possible valid starting positions.
# ----------------------------------------------------------------------------------------------------------------------
"""