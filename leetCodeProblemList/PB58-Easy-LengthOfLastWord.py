"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 58: Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# ----------------------------------------------------------------------------------------------------------------------
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

>Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

>Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

>Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
>Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
# ----------------------------------------------------------------------------------------------------------------------
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        
        wordList = s.split() # Split with no arguments will removes all extra spaces when splitting. If you want to split strictly by a single space, even if there are multiple, you'd have to pass ' ' explicitly. → text.split(' ') # keeps empty strings for multiple spaces
        # print("wordList:", wordList) # Debugging line to see the split words
        if wordList:
            return len(wordList[-1])
        return -1

solution = Solution()
print("Ex1:", solution.lengthOfLastWord("Hello World"))                     # Output: 5
print("Ex2:", solution.lengthOfLastWord("   fly me   to   the moon  "))     # Output: 4
print("Ex3:", solution.lengthOfLastWord("luffy is still joyboy"))           # Output: 6