"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 How do we decide if a for loop should go to n, n-1, or n+1?
# ----------------------------------------------------------------------------------------------------------------------
🚀 It depends on what exactly you want the loop to do.

✅ 1. If you want to do something n times, use:
        for i in range(n):  # From 0 to n-1
    Example: Print "Hello" 5 times? ➔ range(5) → i = 0, 1, 2, 3, 4

✅ 2. If you want to count from 1 to n, use:
        for i in range(1, n+1):  # From 1 to n
    Example: Print numbers 1 → 5? ➔ range(1, 6) → i = 1, 2, 3, 4, 5

✅ 3. If you are starting at 2 (or some specific number), and you want to include n, use:
        for i in range(2, n+1):
    Example: Fibonacci starts calculating from index 2 → you need i = 2, 3, ..., up to n.

✅ 4. If you want to go backward (descending loop), you use:
        for i in range(n, -1, -1):  # From n down to 0
    Example: Countdown timer from 5 to 0.

🎯 Quick Table to Help You Decide:
---------------------------------------------------------
| What you want             | What range to use         |
---------------------------------------------------------
| Repeat something n times  | range(n) (0 to n-1)       |
| Start at 1 and include n  | range(1, n+1)             |
| Start at 2 and include n  | range(2, n+1)             |
| Count down from n to 0    | range(n, -1, -1)          |
---------------------------------------------------------

💡 Fibonacci specific case: In Fibonacci, we already know ..
    - First two values (index 0 and 1) are base cases (0 and 1).
    - So, we start calculating from index 2.
    - We need to calculate until index n → so we do range(2, n+1).

🏆 Super simple way to remember:
    👍 "Always think about: which numbers you want your loop to touch."
    Then adjust your range(start, end) so that the loop covers exactly those numbers.


# [ ➡️ Practice ✨1 ]==================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
🧩 Practice 1: You want to print numbers 0 to 4. What range should you use?
👉 Use: range(5)
    because range(5) ➔ 0, 1, 2, 3, 4

🧩 Practice 2: You want to print numbers 1 to 5. What range should you use?
👉 Use: range(1, 6)
    because range(1, 6) ➔ 1, 2, 3, 4, 5

🧩 Practice 3: You want to count down from 5 to 1. What range should you use?
👉 Use: range(5, 0, -1)
    because it counts: 5, 4, 3, 2, 1

🧩 Practice 4: You already have index 0 and index 1 ready. Now you want to start from index 2 up to index n (include n). What range should you use?
👉 Use: range(2, n+1)
    because it includes 2, 3, ..., n.

🧩 Practice 5: You want to run a loop exactly n times, starting from 0. Which range?
👉 Use: range(n)
    because it loops 0, 1, 2, ..., n-1 (total n times).


# [ ➡️ Practice ✨2 ]==================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
🌟 Next Level Practice 1: Print all even numbers from 1 to n. (Hint: even number = divisible by 2)
    Example: If n = 6, output should be: 2 4 6
✅ Question:
    - What range() should you use?
    - How will you check for even numbers?
# ----------------------------------------------------------------------------------------------------------------------
"""
def nextLvlPractice1(n: int) -> None:
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, end=' ')

print("🌟 Next Level Practice 1:")
nextLvlPractice1(6) # Output: 2 4 6
print("")

"""
# ----------------------------------------------------------------------------------------------------------------------
🌟 Next Level Practice 2: Given a number n, print factorial of n (n × (n-1) × (n-2) × ... × 1)
    Example: If n = 4, factorial = 4 × 3 × 2 × 1 = 24
✅ Question:
    - How to set up the loop to multiply from n down to 1?
# ----------------------------------------------------------------------------------------------------------------------
"""
def nextLvlPractice2(n: int) -> int:
    factorial = 1
    for i in range(n, 0, -1):
#    for i in range(1, n+1):
        factorial *= i
    return factorial

print("🌟 Next Level Practice 2:", nextLvlPractice2(4)) # Output: 24

"""
# ----------------------------------------------------------------------------------------------------------------------
🌟 Next Level Practice 3: Given a list of numbers, find the maximum value manually (without using max()).
    Example: Input: [3, 5, 2, 9, 1] → Output: 9
✅ Question:
    - How will you loop through the list?
    - How to update the "current maximum"?
# ----------------------------------------------------------------------------------------------------------------------
"""
from typing import List

def nextLvlPractice3(nums: List[int]) -> int:
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value

print("🌟 Next Level Practice 3: max_value = ", nextLvlPractice3([3, 5, 2, 9, 1])) # Output: 9

"""
# ----------------------------------------------------------------------------------------------------------------------
🌟 Next Level Practice 4: Given a string s, count how many vowels (a, e, i, o, u) are in it.
    Example: Input: "hello" → Output: 2
✅ Question:
    - How to loop through characters?
    - How to check if a character is a vowel?
# ----------------------------------------------------------------------------------------------------------------------
"""
def nextLvlPractice4(s: str) -> int:
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print("🌟 Next Level Practice 4: count = ", nextLvlPractice4("hello")) # Output: 2

"""
# ----------------------------------------------------------------------------------------------------------------------
🌟 Next Level Practice 5: Given a list of numbers, print numbers in reverse order.
    Example: Input: [1, 2, 3, 4] → Output: 4 3 2 1
✅ Question:
    - How to loop backwards?
    - There are 2 ways: using slicing or using range()!
# ----------------------------------------------------------------------------------------------------------------------
"""
def nextLvlPractice5(nums: List[int]) -> None:
#    for i in range(len(nums)):
#        print(nums[len(nums)-1 - i], end= ' ')
    for num in nums[::-1]:
        print(num, end=' ')

print("🌟 Next Level Practice 5:")
nextLvlPractice5([1, 2, 3, 4]) # Output: 4 3 2 1
print("")


"""
# [ ➡️ Practice ✨3 ]==================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
🌟 Challenge 1: Write a function that checks if a string is a palindrome (same forward and backward).
    - Ignore case ("Racecar" is a palindrome).
    - Ignore non-alphabet characters ("A man, a plan, a canal: Panama" is a palindrome).
    Example:
        is_palindrome("Racecar") ➔ True
        is_palindrome("hello") ➔ False
        is_palindrome("A man, a plan, a canal: Panama") ➔ True
    Hint:
        - Use .lower() to make it lowercase.
        - Use .isalnum() to filter only alphabet/number.
        - Then check if reversed version == original.
# ----------------------------------------------------------------------------------------------------------------------
"""
def is_palindrome(s: str) -> bool:
    s = ''.join(char.lower() for char in s if char.isalnum())
    rs = s[::-1]
    return s == rs

print("[🌟 Challenge 1:]--------------------------------------------------")
print("\t", "is_palindrome(\"Racecar\") =", is_palindrome("Racecar"))   # Output: True
print("\t", "is_palindrome(\"hello\") =", is_palindrome("hello"))       # Output: False
print("\t", "is_palindrome(\"A man, a plan, a canal: Panama\") =", is_palindrome("A man, a plan, a canal: Panama")) # Output: True

"""
# ----------------------------------------------------------------------------------------------------------------------
🌟 Challenge 2 (Bonus): Write a function that returns the second largest number in a list of integers. ⚡No using sort() directly!
    Example:
        second_largest([5, 3, 1, 7, 9]) ➔ 7
        second_largest([99, 44, 22, 100, 88]) ➔ 99
    Hint:
        - Loop and track max1 and max2 manually.
        - Update while looping!
# ----------------------------------------------------------------------------------------------------------------------
"""
def second_largest(nums: List[int]) -> int:
    max1 = max2 = float('-inf') # Initialize to negative infinity
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif max1 > num > max2:
            max2 = num
    return max2

print("[🌟 Challenge 2:]--------------------------------------------------")
print("\t", "second_largest([5, 3, 1, 7, 9]) =", second_largest([5, 3, 1, 7, 9]))               # Output: 7
print("\t", "second_largest([99, 44, 22, 100, 88]) =", second_largest([99, 44, 22, 100, 88]))   # Output: 99
print("\t", "second_largest([-5, -2, -9]) =", second_largest([-5, -2, -9]))                     # Output: -5

"""
# ----------------------------------------------------------------------------------------------------------------------
🌟 Challenge 3: Write a function that counts the frequency of each character in a string and returns it as a dictionary.
    Example:
        char_frequency("hello") ➔ {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        char_frequency("mississippi") ➔ {'m':1, 'i':4, 's':4, 'p':2}
    Hint:
        - Use a dict 📚
        - Loop through each character
# ----------------------------------------------------------------------------------------------------------------------
"""
def char_frequency(s: str) -> dict:
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

from collections import Counter

def char_frequency_shorterVersion(s: str) -> dict:
    return dict(Counter(s))

print("[🌟 Challenge 3:]--------------------------------------------------")
print("\t", "char_frequency(\"hello\") =", char_frequency("hello"))                 # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print("\t", "char_frequency(\"mississippi\") =", char_frequency("mississippi"))     # Output: {'m': 1, 'i': 4, 's': 4, 'p': 2}


"""
# [ ➡️ Practice ✨4 ]==================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
🔥 CHALLENGE (String Compression): Write a function that compresses a string like this:
        ---------------------------------
        | Input         | Output        |
        ---------------------------------
        | "aaabbc"      | "a3b2c1"      |
        | "aabbbaaa"    | "a2b3a3"      |
        | "abc"         | "a1b1c1"      |
        ---------------------------------
    Rules:
        - If a character repeats, count how many times.
        - Compress it into char + count.
        - No spaces in the output.
        - Return the compressed string.
    Hint:
        - Track the current character and current count.
        - When character changes, add old character and count to the result string.
        - Then reset the counter for the new character.
    Note💬:
        ---------------------------------------------------------
        | str[0] would access the first character.              |
        | str[1] would access the second character.             |
        | ...                                                   |
        | str[-2] accesses the second-to-last character.        |
        | str[-1] accesses the character at the last position.  |
        --------------------------------------------------------|
        Python supports negative indexing for sequences like strings, lists, and tuples.
        Instead of starting from 0 at the beginning, negative indices start from -1 at the end and go backwards.
# ----------------------------------------------------------------------------------------------------------------------
"""
def compress_string(s: str) -> str:
    if not s:
        return ""
    
    result_str = ""
    carry_char = ""
    carry_count = 0

    for i, char in enumerate(s):
        if i == 0: # Start with the first character in string s.
            carry_char = char
            carry_count = 1
        else:
            if char == carry_char:
                carry_count += 1
            else:
                result_str += carry_char + str(carry_count)
                carry_char = char
                carry_count = 1
        
    # 🚨 Add the last character and count after the loop ends.
    # -------------------------------------------------------
    # | During the loop → just count and prepare groups.    |
    # | After the loop  → finalize and add the last group.  |
    # -------------------------------------------------------
    # If you add during the loop, you will over-add and get wrong results.
    result_str += carry_char + str(carry_count)

    return result_str

print("[🌟 Practice 4.1:]--------------------------------------------------")
print("\t", "compress_string(\"aaabbc\") = ", compress_string("aaabbc"))            # Output: "a3b2c1"
print("\t", "compress_string(\"aabbbaaa\") =", compress_string("aabbbaaa"))         # Output: "a2b3a3"
print("\t", "compress_string(\"abc\") =", compress_string("abc"))                   # Output: "a1b1c1"
print("\t", "compress_string(\"aabcccccaaa\") =", compress_string("aabcccccaaa"))   # Output: "a2b1c5a3"
print("\t", "compress_string(\"abbcccaa\") =", compress_string("abbcccaa"))         # Output: "a1b2c3a2"
print("\t", "compress_string(\"\") = ", compress_string(""))                        # Output: ""
print("\t", "compress_string(\"a\") =", compress_string("a"))                       # Output: "a1"
print("\t", "compress_string(\"aa\") =", compress_string("aa"))                     # Output: "a2"


"""
# ----------------------------------------------------------------------------------------------------------------------
🔥 HARDER CHALLENGE: Write an advance function compress_string_advanced(s: str) -> str that:
    -----------------------------------------------------------------
    | Input         | Compressed    | Return                        |
    | "aabcccccaaa" | "a2b1c5a3"    | "a2b1c5a3" (shorter)          |
    | "abc"         | "a1b1c1"      | "abc" (original is shorter)   |
    -----------------------------------------------------------------
    Rules:
        - Compresses the string in the same way (character + count).
        - But only returns the compressed version if it's shorter than the original string.
        - Otherwise, return the original string.
# ----------------------------------------------------------------------------------------------------------------------
"""
def compress_string_advanced(s: str) -> str:
    if not s:
        return ""
    
    result_str = ""
    carry_char = ""
    carry_count = 0

    for i, char in enumerate(s):
        if i == 0: # Start with the first character in string s.
            carry_char = char
            carry_count = 1
        else:
            if char == carry_char:
                carry_count += 1
            else:
                result_str += carry_char + str(carry_count)
                carry_char = char
                carry_count = 1
        
    # 🚨 Add the last character and count after the loop ends.
    # -------------------------------------------------------
    # | During the loop → just count and prepare groups.    |
    # | After the loop  → finalize and add the last group.  |
    # -------------------------------------------------------
    # If you add during the loop, you will over-add and get wrong results.
    result_str += carry_char + str(carry_count)

    if len(result_str) < len(s):
        return result_str
    else:
        return s

print("[🌟 Practice 4.2:]--------------------------------------------------")
print("\t", "compress_string_advanced(\"aabcccccaaa\") =", compress_string_advanced("aabcccccaaa"))     # Output: "a2b1c5a3"
print("\t", "compress_string_advanced(\"abc\") =", compress_string_advanced("abc"))                     # Output: "abc"
print("\t", "compress_string_advanced(\"\") =", compress_string_advanced(""))                           # Output: ""
print("\t", "compress_string_advanced(\"aabb\") =", compress_string_advanced("aabb"))                   # Output: "aabb"
print("\t", "compress_string_advanced(\"aabbcc\") =", compress_string_advanced("aabbcc"))               # Output: "aabbcc"
print("\t", "compress_string_advanced(\"aaabb\") =", compress_string_advanced("aaabb"))                 # Output: "a3b2"


"""
# [ ➡️ Practice ✨5 ]==================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
🧩 CRAZY CHALLENGE: Write a function def compress_string_recursive(s: str) -> str:
    Requirements:
        - Use Recursion (not for / while loops).
        - Compress the string like before: "aabcccccaaa" → "a2b1c5a3".
        - If the compressed string is not shorter, return the original string.
    Hints:
        - Use recursion to move through the string character by character.
        - Carry the current character and its count during recursion.
        - At the end, decide whether to return the original or compressed.
    Example:
        compress_string_recursive("aabcccccaaa")  -->  "a2b1c5a3"
        compress_string_recursive("abc")          -->  "abc"
        compress_string_recursive("")             -->  ""
    Note💬:
        -------------------------------------------------
        | def compress_string_recursive(s: str) -> str: |
        |     pass                                      |
        -------------------------------------------------
        # In Python, the keyword "pass" (a placeholder) simply means: "Do nothing, I'll write the code later".
        # It’s used when you have to put something (because Python doesn’t allow an empty block), but you don’t want the code to do anything yet.
        # You’ve defined the function, but inside it, you haven’t written any real code yet — you just put pass there to avoid syntax errors.
# ----------------------------------------------------------------------------------------------------------------------
"""
def compress_string_recursive(s: str) -> str:
    if not s:
        return ""

    def _compress(index, current_char, count):
        if index == len(s): # The last character
            return current_char + str(count)

        if s[index] == current_char:
            return _compress(index + 1, current_char, count + 1)
        else:
            return current_char + str(count) + _compress(index + 1, s[index], 1)

    compressed = _compress(1, s[0], 1)
    return compressed if len(compressed) < len(s) else s

print("[🧩 CRAZY CHALLENGE:]--------------------------------------------------")
print("\t", "compress_string_recursive(\"aabcccccaaa\") =", compress_string_recursive("aabcccccaaa"))   # Output: "a2b1c5a3"
print("\t", "compress_string_recursive(\"abc\") =", compress_string_recursive("abc"))                   # Output: "abc"
print("\t", "compress_string_recursive(\"\") =", compress_string_recursive(""))                         # Output: ""
print("\t", "compress_string_recursive(\"aabb\") =", compress_string_recursive("aabb"))                 # Output: "aabb"
print("\t", "compress_string_recursive(\"aabbcc\") =", compress_string_recursive("aabbcc"))             # Output: "aabbcc"
print("\t", "compress_string_recursive(\"aaabb\") =", compress_string_recursive("aaabb"))               # Output: "a3b2"


"""
# [ ➡️ Practice ✨6 ]==================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
💪 Challenge: Longest Palindromic Substring
    Write a function that finds the longest palindromic substring in a given string s.
    Function Signature:
        def longest_palindrome(s: str) -> str:
    Example:
        longest_palindrome("babad")  # Output: "bab" or "aba"
        longest_palindrome("cbbd")   # Output: "bb"
    Constraints
        - You may assume s has a length between 1 and 1000.
        - You should aim for an efficient solution (better than brute force).
    Hints: 
        1. A Palindrome Expands from the Center
            Every palindrome mirrors around its center. For example, "racecar" has a center at 'e' and expands outwards.
            You can expand around every possible center (including centers between characters like in "abba") and find the longest palindrome that way.
        2. Odd and Even Lengths
            You need to consider both:
                Odd-length centers (like "aba" → center at 'b')
                Even-length centers (like "abba" → center between 'b's)
            For each center, expand outward as long as the characters match.
        3. Use a Helper Function
            Write a helper function like: def expand_from_center(left: int, right: int) -> str:
            It should return the longest palindrome by expanding outward from the given indices
# ----------------------------------------------------------------------------------------------------------------------
"""
def longest_palindrome(s: str) -> str:
    if not s or len(s) == 1:
        return s
    
    def expand_from_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome : centered at i
        odd = expand_from_center(i, i)
        # Even-length palindrome : centered at i and i + 1
        even = expand_from_center(i, i + 1)
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    return longest

print("[💪 Longest Palindromic Substring:]--------------------------------------------------")
print("\t", "longest_palindrome(\"babad\") =", longest_palindrome("babad"))     # Output: "bab" or "aba"
print("\t", "longest_palindrome(\"cbbd\") =", longest_palindrome("cbbd"))       # Output: "bb"