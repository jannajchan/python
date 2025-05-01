"""
# ----------------------------------------------------------------------------------------------------------------------
# Problem 383: Ransom Note
# https://leetcode.com/problems/ransom-note/
# ----------------------------------------------------------------------------------------------------------------------
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

>Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
✏️ Explanation:
    ➔ You need one 'a'
    ➔ Magazine only has 'b'
    ❌ Not enough letters → return False

>Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
✏️ Explanation:
    ➔ You need two 'a's
    ➔ Magazine has one 'a' and one 'b'
    ❌ Not enough 'a's → return False

>Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
✏️ Explanation:
    ➔ You need two 'a's
    ➔ Magazine has two 'a's and one 'b'
    ✅ You can build it → return True
 
>Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
# ----------------------------------------------------------------------------------------------------------------------
📝 Note:
    You are given two strings:
    - ransomNote: the string you want to construct
    - magazine: the string that contains available letters
    Your task is to check if you can build the ransomNote using the letters in magazine.

Important Rule:
    You can only use each letter in magazine once.

⚠️ Strings are immutable (Cannot be changed).
# ----------------------------------------------------------------------------------------------------------------------
"""

class Solution:
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        def _containerMapping(s: str) -> dict:
            hash = {}
            for char in s:
                if char in hash:
                    hash[char] += 1
                else:
                    hash[char] = 1
            return hash

        ransomNoteMapping = _containerMapping(ransomNote)
        magazineMapping = _containerMapping(magazine)
        #print("ransomNoteMapping:", ransomNoteMapping, "| magazineMapping:", magazineMapping)

        for char, count in ransomNoteMapping.items():
            if char not in magazineMapping or magazineMapping[char] < count:
                return False
        return True
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool: #👏😎
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,"",1)
            else: return False
        
        return True

solution = Solution()
print("Ex1:", solution.canConstruct("a", "b"))      # Output: False
print("Ex2:", solution.canConstruct("aa", "ab"))    # Output: False
print("Ex3:", solution.canConstruct("aa", "aab"))   # Output: True