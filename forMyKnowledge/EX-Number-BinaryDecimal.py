import re
from typing import List, NamedTuple, Tuple

"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 Convert between decimal and binary number.
# ----------------------------------------------------------------------------------------------------------------------
"""

"""
# [💪 Challenge ✨1] Convert string (binary) <-> integer (decimal) ====================================================
# ----------------------------------------------------------------------------------------------------------------------
"""
def binaryStr_to_decimalInt_manual(binary_str: str) -> int:         # Manual conversion with a loop using powers of 2.
    decimal = 0
    for i, bit in enumerate(reversed(binary_str)):
        decimal += int(bit) * (2 ** i)
    return decimal

def binaryStr_to_decimalInt(binary_str: str) -> int:                # Using int() with base 2.
    return int(binary_str, 2)

def decimalInt_to_binaryStr_manual(decimal_int: int) -> str:        # Manually using modulo and integer division.
    binary_str = ""
    # Explanation: Keep dividing by 2, store the remainder, and build the binary string from right to left.
    while decimal_int > 0:
        binary_str = str(decimal_int % 2) + binary_str
        decimal_int //= 2       # Use integer division // instead of float division / to avoid float errors.
    return binary_str

def decimalInt_to_binaryStr_format(decimal_int: int) -> str:
    return format(decimal_int, 'b')

def decimalInt_to_binaryStr(decimal_int: int) -> str:
    return bin(decimal_int)[2:]

def binaryAddition(decimal_int_a: int, decimal_int_b: int) -> str:
    return bin(decimal_int_a + decimal_int_b)[2:]

def binaryAddition(binary_str_a: str, binary_str_b: str) -> str:
    return bin(binaryStr_to_decimalInt(binary_str_a) + binaryStr_to_decimalInt(binary_str_b))[2:]

print("\n[💪 Challenge ✨1] Convert string (binary) to integer (decimal) -----------------")
print("\t", binaryStr_to_decimalInt_manual("1010"))                 # Output: 10
print("\t", binaryStr_to_decimalInt_manual("1101"))                 # Output: 13
print("\t", binaryStr_to_decimalInt_manual("100000"))               # Output: 32
print("\t", binaryStr_to_decimalInt("1010"))                        # Output: 10
print("\t", binaryStr_to_decimalInt("1101"))                        # Output: 13
print("\t", decimalInt_to_binaryStr_manual(10))                     # Output: "1010"
print("\t", decimalInt_to_binaryStr_manual(15))                     # Output: "1111"
print("\t", decimalInt_to_binaryStr_manual(32))                     # Output: "100000"
print("\t", decimalInt_to_binaryStr_format(10))                     # Output: "1010"
print("\t", decimalInt_to_binaryStr_format(13))                     # Output: "1101"
print("\t", decimalInt_to_binaryStr(10))                            # Output: "1010"
print("\t", decimalInt_to_binaryStr(13))                            # Output: "1101"
print("\t", binaryAddition("11", "1"))                              # Output: "100"
print("\t", binaryAddition("1010", "1011"))                         # Output: "10101"


"""
# [💪 Challenge ✨2.1] Count Binary Ones ==============================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Goal: Return how many 1s are in the binary string.
    Function Signature:
        def count_binary_ones(binary_str: str) -> int:
            pass
    Example:
        count_binary_ones("110101")                                 # Output: 4
        count_binary_ones("0000")                                   # Output: 0
# ----------------------------------------------------------------------------------------------------------------------
"""
def count_binary_ones(binary_str: str) -> int:
    count = 0
    for i in range(len(binary_str)):
        if binary_str[i] == "1":
            count += 1
    return count

def count_binary_ones_simplify(binary_str: str) -> int:
    return binary_str.count("1")

print("\n[💪 Challenge ✨2.1] Count Binary Ones ------------------------------------------")
print("\t", count_binary_ones("110101"))                            # Output: 4
print("\t", count_binary_ones("0000"))                              # Output: 0


"""
# [💪 Challenge ✨2.2] Is Power of Two? ===============================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Goal: Convert binary to decimal and return whether it’s a power of 2.
    Function Signature:
        def is_power_of_two(binary_str: str) -> bool:
            pass
    Example:
        is_power_of_two("100") #4                                   # Output: True
        is_power_of_two("110") #6                                   # Output: False
# ----------------------------------------------------------------------------------------------------------------------
"""
def is_power_of_two(binary_str: str) -> bool:
    binary_int = int(binary_str, 2)
    if binary_int <= 0:             # Zero or Negative number
        return False
    elif binary_int % 2 != 0:       # Odd number
        return False        
    else:
        while binary_int > 1:
            if binary_int % 2 == 0:
                binary_int //= 2    # Use integer division // instead of float division / to avoid float errors.
            else:
                return False
        return True

def is_power_of_two_improvedVersion(binary_str: str) -> bool:
    n = int(binary_str, 2)
    return n > 0 and (n & (n - 1)) == 0

print("\n[💪 Challenge ✨2.2] Is Power of Two? -------------------------------------------")
print("\t", is_power_of_two("100")) #4                              # Output: True
print("\t", is_power_of_two("110")) #6                              # Output: False
print("\t", is_power_of_two(decimalInt_to_binaryStr(8)))            # Output: True
print("\t", is_power_of_two(decimalInt_to_binaryStr(64)))           # Output: True
print("\t", is_power_of_two(decimalInt_to_binaryStr(200)))          # Output: False
print("\t", is_power_of_two(decimalInt_to_binaryStr(13)))           # Output: False


"""
# [💪 Challenge ✨2.3] Binary Addition ================================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Goal: Add two binary strings and return the binary result.
    Function Signature:
        def add_binary(a: str, b: str) -> str:
            pass
    Example:
        add_binary("1010", "1011")                                  # Output: "10101"  # 10 + 11 = 21
# ----------------------------------------------------------------------------------------------------------------------
"""
def binary_add(binary_str_a: str, binary_str_b: str) -> str:
    return bin(int(binary_str_a, 2) + int(binary_str_b, 2))[2:]

print("\n[💪 Challenge ✨2.3] Binary Addition --------------------------------------------")
print("\t", binary_add("1010", "1011"))                             # Output: "10101"


"""
# [💪 Challenge ✨2.4] Reverse Bits ===================================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Goal: Return the binary string reversed (e.g., for little-endian simulation).
    Function Signature:
        def reverse_bits(binary_str: str) -> str:
            pass
    Example:
        reverse_bits("11001")                                       # Output: "10011"
# ----------------------------------------------------------------------------------------------------------------------
"""
def reverse_bits(binary_str: str) -> str:
    return binary_str[::-1]

print("\n[💪 Challenge ✨2.4] Reverse Bits -----------------------------------------------")
print("\t", reverse_bits("1010"))                                   # Output: "0101"
print("\t", reverse_bits("11001"))                                  # Output: "10011"


"""
# [💪 Challenge ✨2.5] Invert Bits ====================================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Goal: Return the binary string inverted (e.g., for 1→0, 0→1)
    Function Signature:
        def invert_bits(binary_str: str) -> str:
            pass
    Example:
        invert_bits("1010")                                         # Output: "0101"
# ----------------------------------------------------------------------------------------------------------------------
"""
def invert_bits(binary_str: str) -> str:
    invert_bits = ""
    for i in range(len(binary_str)):
        if binary_str[i] == "1":
            invert_bits += "0"
        elif binary_str[i] == "0":
            invert_bits += "1"
        else:
            return "Invalid binary string format."
    return invert_bits

def invert_bits_improvedVersion(binary_str: str) -> str:
    return ''.join('0' if bit == '1' else '1' if bit == '0' else '?' for bit in binary_str)

print("\n[💪 Challenge ✨2.5] Invert Bits ------------------------------------------------")
print("\t", invert_bits("1010"))                                    # Output: "0101"
print("\t", invert_bits("11001"))                                   # Output: "00110"


"""
🌟 Awesome! Here are some medium-to-advanced binary challenges to level up your skills: 🌟

# [💪 Challenge ✨3.1] Find the Longest Binary Gap ====================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: A binary gap is the longest sequence of consecutive zeros surrounded by ones in the binary representation of a number.
    Function Signature:
        def longest_binary_gap(binary_str: str) -> int:
            pass
    Example:
        Input: "1001000100001"                                      # Output: 4 (Longest sequence of 4 zeros between two 1s)
# ----------------------------------------------------------------------------------------------------------------------
"""
def longest_binary_gap(binary_str: str) -> int:
    if not binary_str:
        return 0
    strList = binary_str.strip("0").split("1")      # Add strip("0") to remove leading/trailing zeros — these can't be part of a binary gap.
    longest = 0
    for i in range(len(strList)):
        if longest < len(strList[i]):
            longest = len(strList[i])
    return longest

print("\n[💪 Challenge ✨3.1] Find the Longest Binary Gap --------------------------------")
print("\t", longest_binary_gap("1001000100001"))                    # Output: 4
print("\t", longest_binary_gap("1000001010001"))                    # Output: 5


"""
# [💪 Challenge ✨3.2] Count Bit Flips to Convert A to B ==============================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Given two binary strings of equal length, count how many bits need to be flipped to convert one to the other.
    Function Signature:
        def count_bit_flips(binary_str_a: str, binary_str_b: str) -> int:
            pass
    Example:
        a = "1101"
        b = "1001"
        Output: 1  # Only one bit differs at index 1
# ----------------------------------------------------------------------------------------------------------------------
"""
def count_bit_flips(binary_str_a: str, binary_str_b: str) -> int:
    if len(binary_str_a) != len(binary_str_b):      # Check for equal length, just in case.
        raise ValueError("Binary strings must be the same length.")
    count = 0
    for i in range(len(binary_str_a)):
        if binary_str_a[i] != binary_str_b[i]:
            count += 1
    return count

print("\n[💪 Challenge ✨3.2] Count Bit Flips to Convert A to B --------------------------")
print("\t", count_bit_flips("1101", "1001"))                        # Output: 1
print("\t", count_bit_flips("10101", "11011"))                      # Output: 3


"""
# [💪 Challenge ✨3.3] Binary Rotation (Rotate right by k-bit.) =======================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Rotate the binary string right by k positions.
    Function Signature:
        def binary_rotate_right(s: str, k: int) -> str:
            pass
    Example:
        Input: s = "1011001", k = 2
        Output: "0110110"
# ----------------------------------------------------------------------------------------------------------------------
"""
def binary_rotate_right(binary_str: str, k: int) -> str:
    if not binary_str:
        return ""
    k = k % len(binary_str) # To handle case rotations > length
    return binary_str[-k:] + binary_str[:-k]

print("\n[💪 Challenge ✨3.3] Binary Rotation (Rotate right by k-bit.) -------------------")
print("\t", binary_rotate_right("1011001", 2))                      # Output: "0110110"
print("\t", binary_rotate_right("1011", 5))                         # Output: "1101"


"""
# [💪 Challenge ✨3.4] Binary AND of a Range ==========================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Given two binary numbers start and end, perform bitwise AND of all integers in the inclusive range [start, end].
    Function Signature:
        def and_binary(binary_str_a: str, binary_str_b: str) -> str:
            pass
    Example:
        Input: "1010" to "1101"  (decimal: 10 to 15)
        Output: "1000"
# ----------------------------------------------------------------------------------------------------------------------
"""
def binary_and(binary_str_a: str, binary_str_b: str) -> str:
    return bin(int(binary_str_a, 2) & int(binary_str_b, 2))[2:]

print("\n[💪 Challenge ✨3.4] Binary AND of a Range --------------------------------------")
print("\t", binary_and("1010", "1101"))                             # Output: "1000"


"""
# [💪 Challenge ✨3.5] Binary Palindrome Check ========================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Determine if a binary string is a palindrome.
        (Palindrome Number is a number (such as 16361) that remains the same when its digits are reversed. In other words, it has reflectional symmetry across a vertical axis.)
    Function Signature:
        def is_binary_palindrome(binary_str: str) -> bool:
            pass
    Example:
        Input: "1001"
        Output: True
# ----------------------------------------------------------------------------------------------------------------------
"""
def is_binary_palindrome(binary_str: str) -> bool:
    if not binary_str:
        return False
    return binary_str[::-1] == binary_str

print("\n[💪 Challenge ✨3.5] Binary Palindrome Check ------------------------------------")
print("\t", is_binary_palindrome("1001"))                           # Output: True


"""
🌟 Here are 5 progressively harder binary-related challenges to sharpen your skills in binary string manipulation, bit operations, and logic: 🌟

# [💪 Challenge ✨4.1.1] Binary XOR Palindrome ========================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Given a binary string, flip at most one bit (0 to 1 or 1 to 0) to make it a palindrome. Return True if possible, else False.
        (A binary string is a palindrome if it reads the same forwards and backwards. Example: "1001", "11111", "0" are palindromes.)
    Function Signature:
        def is_binary_xor_palindrome(binary_str: str) -> bool:
            pass
    Example:
        is_binary_xor_palindrome("10101")                           # Output: True
    Hints:
        Count mismatched bit pairs from both ends.
             0 mismatches → already a palindrome                    # Output: True
             1 mismatch   → flip one bit to fix it                  # Output: True
            >1 mismatches → cannot fix with a single flip           # Output: False
# ----------------------------------------------------------------------------------------------------------------------
"""
def is_binary_xor_palindrome(binary_str: str) -> bool:
    if not binary_str:
        return False
    
    mismatch_count = 0
    for i in range(len(binary_str) // 2):
        if binary_str[i] != binary_str[-(i+1)]:
            mismatch_count += 1
    
    return mismatch_count <= 1

print("\n[💪 Challenge ✨4.1.1] Binary XOR Palindrome ------------------------------------")
print("\t", is_binary_xor_palindrome("10101"))                      # Output: True  (already a palindrome)
print("\t", is_binary_xor_palindrome("1101"))                       # Output: True  (flip one bit)
print("\t", is_binary_xor_palindrome("10010"))                      # Output: False (need more than one flip)
print("\t", is_binary_xor_palindrome(""))                           # Output: False (empty)
print("\t", is_binary_xor_palindrome("0"))                          # Output: True  (single char)


"""
# [💪 Challenge ✨4.1.2] Binary k-flips Palindrome ====================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Check whether the binary string can be converted into a palindrome by flipping at most k bits.
    Function Signature:
        def is_binary_k_flips_palindrome(binary_str: str, k: int) -> bool:
            pass
    Example:
        is_binary_k_flips_palindrome("10011", 1)                    # Output: True
    Hints: (Step-by-Step Idea)
        1. Compare symmetric characters: Loop through the string from both ends.
        2. Count mismatches: Each mismatch means a flip is needed.
        3. Check if flips needed ≤ k.
# ----------------------------------------------------------------------------------------------------------------------
"""
def is_binary_k_flips_palindrome(binary_str: str, k: int) -> bool:
    mismatch_count = 0
    for i in range(len(binary_str) // 2):
        if binary_str[i] != binary_str[-(i+1)]:
            mismatch_count += 1
    return mismatch_count <= k

print("\n[💪 Challenge ✨4.1.2] Binary k-flips Palindrome ----------------------------------")
print("\t", is_binary_k_flips_palindrome("10011", 1))               # Output: True      # Flip '0' at index 1 → "11011"
print("\t", is_binary_k_flips_palindrome("10011", 0))               # Output: False     # Needs 1 flip, but allowed = 0
print("\t", is_binary_k_flips_palindrome("10101", 0))               # Output: True      # Already a palindrome
print("\t", is_binary_k_flips_palindrome("11000", 2))               # Output: True      # Flip index 1 & 4 → "10001"
print("\t", is_binary_k_flips_palindrome("10010", 1))               # Output: False     # Need 2 flips, but allowed = 1
print("\t", is_binary_k_flips_palindrome("1001", 0))                # Output: True      # Already a palindrome


"""
# [💪 Challenge ✨4.2] Binary Mirror Reflection =======================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Write a function that returns the mirror image of a binary string. A "mirror image" means reverse the bits and also flip them (0→1, 1→0).
    Function Signature:
        def binary_mirror_reflect(binary_str: str) -> str:
            pass
    Example:
        "1010" → reversed: "0101" → flipped: "1010"                 # Output: "1010"
# ----------------------------------------------------------------------------------------------------------------------
"""
def binary_mirror_reflect(binary_str: str) -> str:
    reversed_str = binary_str[::-1]                                 # Reverse binary string.
    flipped_str = reversed_str[-1:] + reversed_str[:-1]             # Rotate right by 1-bit.
    return flipped_str

def binary_mirror_pure_reverse(binary_str: str) -> str:
    return binary_str[::-1]

def binary_bitwise_mirror_flip(binary_str: str) -> str:
    return ''.join('1' if bit == '0' else '0' for bit in binary_str[::-1])

print("\n[💪 Challenge ✨4.2] Binary Mirror Reflection -----------------------------------")
print("\t", binary_mirror_reflect("1011"))                          # Output: "1110"
print("\t", binary_mirror_reflect("10110"))                         # Output: "10110"


"""
# [💪 Challenge ✨4.3] Max Consecutive 1s with One Flip ===============================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Given a binary string, return the length of the longest sequence of 1s you can get by flipping at most one 0 to 1.
    Function Signature:
        def max_consecutive_1s(binary_str: str) -> int:
            pass
    Example:
        "1101011" → flip 0 at index 3 → "1101111" → longest = 5     # Output: 5
    Hints:
        Step 1: Split the string by '0' to find all blocks of consecutive '1's separated by '0's.
                Don't removes leading and trailing zeroes (.strip()) which may lose potential flip opportunities at the edges.
        Step 2: Identify the gaps between '1' blocks.
                Wherever there is a single '0' between two '1' groups, that's a candidate to flip. Flipping that 0 will merge two '1' blocks into one longer block.
        Step 3: Walk through the string, count consecutive '1's by moving through the binary string one character at a time.
                If you hit a '0', track how many '1's are on the left and right of it.
        Step 4: Consider the best place to flip 0→1.
                For every '0':
                    - Calculate: left_ones + 1 (for flipped 0) + right_ones
                    - Keep track of the maximum total you can get from any such flip.
        Step 5: Handle edge cases.
                    - If there are no '0's, return the length of the entire string (all 1s).
                    - If there's only one '0', flipping it gives you full length.
                    - If the string is all '0's, flipping one gives max 1.
        Step 6: Return the Maximum.
                After evaluating all possible flips, return the maximum sequence length found.

# ----------------------------------------------------------------------------------------------------------------------
"""
def max_consecutive_1s(binary_str: str) -> int:
    if not binary_str:
        return 0
    
    # Split the string by '0' to find all blocks of consecutive 1s
    ones_block = binary_str.split('0')
    max_consecutive = 0

    if binary_str.count("0") <= 1:      # No '0' to flip (already longest sequence), or there's only one '0' (flipping it gives you full length) → return the length of the entire string (all 1s).
        return len(binary_str)
    
    if binary_str.count("1") == 0:      # All characters are '0' → max '0' to flip in this challenge is 1.
        return 1
    
    for i in range(len(ones_block) - 1):
        # Combine two blocks of 1s around a single 0, adding 1 for the flipped 0.
        combined = len(ones_block[i]) + 1 + len(ones_block[i+1])
        max_consecutive = max(max_consecutive, combined)

    # Also check if flipping a single 0 gives max with just one block + 1
    for block in ones_block:
        max_consecutive = max(max_consecutive, len(block) + 1)

    return max_consecutive

print("\n[💪 Challenge ✨4.3] Max Consecutive 1s with One Flip ---------------------------")
print("\t", max_consecutive_1s("1101011"))                          # Output: 4
print("\t", max_consecutive_1s("10001"))                            # Output: 2
print("\t", max_consecutive_1s("1111"))                             # Output: 4
print("\t", max_consecutive_1s("0000"))                             # Output: 1
print("\t", max_consecutive_1s("101010"))                           # Output: 3
print("\t", max_consecutive_1s("11011101111"))                      # Output: 8
print("\t", max_consecutive_1s("1011101110"))                       # Output: 7


"""
# [💪 Challenge ✨4.4] Binary Substring Match Count ===================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Given a binary string s and a pattern p, count how many times p appears as a substring in s, allowing overlapping matches.
    Function Purpose:
        It counts how many times a binary pattern appears in a larger binary string — including overlapping occurrences.
    Function Signature:
        def binary_substring_match_count(binary_str: str, pattern_str: str) -> int:
            pass
    Example:
        s = "1010101", p = "101" → appears at indices 0 and 2 → count = 2   # Output: 2
# ----------------------------------------------------------------------------------------------------------------------
"""
def binary_substring_match_count(binary_str: str, pattern_str: str) -> int:
    match_count = 0
    for i in range(len(binary_str) - len(pattern_str) + 1):
        if binary_str[i:i+len(pattern_str)] == pattern_str:
            match_count += 1
    return match_count

print("\n[💪 Challenge ✨4.4] Binary Substring Match Count -------------------------------")
print("\t", binary_substring_match_count("1010101", "101"))         # Output: 3
print("\t", binary_substring_match_count("11011011", "11"))         # Output: 3
print("\t", binary_substring_match_count("101010", "10"))           # Output: 3
print("\t", binary_substring_match_count("1111", "11"))             # Output: 3
print("\t", binary_substring_match_count("000", "1"))               # Output: 0


"""
# [💪 Challenge ✨4.5] Binary Substring match with wildcard ===========================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Count how many times the given pattern appears in the binary string, where the pattern can contain ? as a wildcard character.
        (The return value is the total number of matches found — an int.)
    Function Signature:
        def binary_substring_match_with_wildcard(binary_str: str, pattern: str) -> int:
            pass
    Example:
        binary_substring_match_with_wildcard("101010", "1?0")
# ----------------------------------------------------------------------------------------------------------------------
"""
def binary_substring_match_with_wildcard(binary_str: str, pattern_str: str) -> int:
    match_count = 0
    for i in range(len(binary_str) - len(pattern_str) + 1):
        segment = binary_str[i:i+len(pattern_str)]
        match = True
        for j in range(len(pattern_str)):
            if pattern_str[j] != '?' and pattern_str[j] != segment[j]:
                match = False
                break
        if match:
            match_count += 1
    return match_count

print("\n[💪 Challenge ✨4.5] Binary Substring match with wildcard -----------------------")
print("\t", binary_substring_match_with_wildcard("101010", "1?0"))      # Output: 0
print("\t", binary_substring_match_with_wildcard("11001010", "1?0"))    # Output: 2
# TODO Would you like to try extending this to support multiple wildcards like * (for zero or more bits) as well?


"""
# [💪 Challenge ✨4.6] Bitwise Majority ===============================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Given three binary strings of equal length, return a new binary string where each bit is the majority of the three at that position.
    Function Purpose:
        For each bit position, return the bit that appears at least twice among the three input strings.
            Giving: A = "1101", B = "1001", C = "1110"
            --------------------------
            |   A   B   C   Majority |
            |   1   1   1       1    |
            |   1   0   1       1    |
            |   0   0   1       0    |
            |   1   1   0       1    |
            --------------------------
    Function Signature:
        def bitwise_majority(binary_str_a: str, binary_str_b: str, binary_str_c: str) -> str:
            pass
    Example:
        a = "1101"
        b = "1001"
        c = "1010"
        → Output: "1001"  # bitwise majority at each position
    Hints: To find the majority bit, you should count how many 1s are present at each index, and set that bit to "1" if 1s appear at least twice.
# ----------------------------------------------------------------------------------------------------------------------
"""
def bitwise_majority(binary_str_a: str, binary_str_b: str, binary_str_c: str) -> str:
    def _is_char_one(char: str) -> bool:                # Cleanly checks if a character is '1'.
        return True if char == '1' else False
    
    def _count_char_one(charList: List[str]) -> int:    # Counts how many '1's appear in a list of bits.
        count = 0
        for char in charList:
            if _is_char_one(char):
                count += 1
        return count
    
    # Looping through bit positions:
    #   – At each index, checks how many of the three input bits are '1'.
    #   – If two or more, appends '1'; otherwise, '0'.
    majority = ""
    for i in (range(len(binary_str_a))):
        one_count = _count_char_one([binary_str_a[i], binary_str_b[i], binary_str_c[i]])
        if one_count >= 2:
            majority += '1'
        else:
            majority += '0'
    return majority

# Python has built-in tools like sum() and list comprehensions that can simplify code without losing readability.
def bitwise_majority_improvedVersion(binary_str_a: str, binary_str_b: str, binary_str_c: str) -> str:
    majority = ""
    for i in range(len(binary_str_a)):
        one_count = sum(c == '1' for c in [binary_str_a[i], binary_str_b[i], binary_str_c[i]])
        majority += '1' if one_count >= 2 else '0'
    return majority

print("\n[💪 Challenge ✨4.6] Bitwise Majority -------------------------------------------")
print("\t", bitwise_majority("1101", "1001", "1010"))               # Output: "1001"
print("\t", bitwise_majority("1101", "1001", "1110"))               # Output: "1101"


"""
# [💪 Challenge ✨5.1] Bitwise Disagreement Map =======================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Return a binary string where each bit is '1' if not all values agree (some are '0', some are '1'), and '0' otherwise.
    Function Signature:
        def bitwise_disagreement(binary_str_list: List[str]) -> str:
            pass
    Example:
        Input: ["1010", "1011", "1000"]                             # Output: "0011"
# ----------------------------------------------------------------------------------------------------------------------
"""
def bitwise_disagreement(binary_str_list: List[str]) -> str:
    disagreement = ""
    for i in range(len(binary_str_list[0])):                        # Number of characters in the string (each bit position).
        one_count = 0
        for j in range(len(binary_str_list)):                       # Number of elements in the list (each binary string).
            one_count += 1 if binary_str_list[j][i] == '1' else 0
        disagreement += '1' if 0 < one_count < len(binary_str_list) else '0'    # Returns '1' only if some string has '1' and other have '0' at that position. If all strings have the same bit (all '0' or all '1'), returns '0'.
    return disagreement

print("\n[💪 Challenge ✨5.1] Bitwise Disagreement Map -----------------------------------")
print("\t", bitwise_disagreement(["1010", "1011", "1000"]))         # Output: "0011"
print("\t", bitwise_disagreement(["1110", "1101", "1111"]))         # Output: "0011"
print("\t", bitwise_disagreement(["1101", "1111", "1101"]))         # Output: "0010"
print("\t", bitwise_disagreement(["111", "101", "111"]))            # Output: "010"
print("\t", bitwise_disagreement(["110", "111", "100"]))            # Output: "011"


"""
# [💪 Challenge ✨5.2] Bitwise Super Majority =========================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Given a list of n binary strings of equal length, return a new binary string where each bit is '1' if more than half of the strings have '1' at that position.
    Function Signature:
        def bitwise_super_majority(binary_str_list: List[str]) -> str:
            pass
    Example:
        Input: ["1010", "1111", "0010", "1011", "1110"]             # Output: "1010"
# ----------------------------------------------------------------------------------------------------------------------
"""
def bitwise_super_majority(binary_str_list: List[str]) -> str:
    super_majority = ""
    for i in range(len(binary_str_list[0])):                        # Number of characters in the string (each bit position).
        one_count = 0
        for j in range(len(binary_str_list)):                       # Number of elements in the list (each binary string).
            one_count += 1 if binary_str_list[j][i] == '1' else 0
        super_majority += '1' if one_count > len(binary_str_list) / 2 else '0'  # Returns '1' only if more than half of the strings have '1'. Otherwise, returns '0'.
    return super_majority

print("\n[💪 Challenge ✨5.2] Bitwise Super Majority -------------------------------------")
print("\t", bitwise_super_majority(["1010", "1111", "0010", "1011", "1110"]))   # Output: "1010"


"""
# [💪 Challenge ✨5.3] Consensus AND ==================================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Return a binary string where each bit is '1' only if all strings have '1' at that position (bitwise AND across all).
    Function Signature:
        def consensus_and(binary_str_list: List[str]) -> str:
            pass
    Example:
        Input: ["1110", "1101", "1111"]                             # Output: "1100"
# ----------------------------------------------------------------------------------------------------------------------
"""
def consensus_and(binary_str_list: List[str]) -> str:
    consensus_mask = ""
    for i in range(len(binary_str_list[0])):                        # Number of characters in the string (each bit position).
        one_count = 0
        for j in range(len(binary_str_list)):                       # Number of elements in the list (each binary string).
            one_count += 1 if binary_str_list[j][i] == '1' else 0
        consensus_mask += '1' if one_count == len(binary_str_list) else '0'     # Returns '1' only if every string has '1' at that position. Otherwise, returns '0'.
    return consensus_mask

print("\n[💪 Challenge ✨5.3] Consensus AND ----------------------------------------------")
print("\t", consensus_and(["1110", "1101", "1111"]))                # Output: "1100"
print("\t", consensus_and(["1101", "1111", "1101"]))                # Output: "1101"
print("\t", consensus_and(["111", "101", "111"]))                   # Output: "101"
print("\t", consensus_and(["110", "111", "100"]))                   # Output: "100"


"""
# [💪 Challenge ✨5.4] Consensus OR ===================================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: Return a binary string where each bit is '1' only if at least one string have '1' at that position (bitwise OR across all).
    Function Signature:
        def consensus_or(binary_str_list: List[str]) -> str:
            pass
    Example:
        Input: ["1110", "1101", "1111"]                             # Output: "1111"
# ----------------------------------------------------------------------------------------------------------------------
"""
def consensus_or(binary_str_list: List[str]) -> str:
    consensus_mask = ""
    for i in range(len(binary_str_list[0])):                        # Number of characters in the string (each bit position).
        one_count = 0
        for j in range(len(binary_str_list)):                       # Number of elements in the list (each binary string).
            one_count += 1 if binary_str_list[j][i] == '1' else 0
        consensus_mask += '1' if one_count > 0 else '0'             # Returns '1' only if at least one string has '1' at that position. If all string have '0', returns '0'.
    return consensus_mask

print("\n[💪 Challenge ✨5.4] Consensus OR -----------------------------------------------")
print("\t", consensus_or(["1110", "1101", "1111"]))                 # Output: "1111"
print("\t", consensus_or(["1101", "1111", "1101"]))                 # Output: "1111"
print("\t", consensus_or(["111", "101", "111"]))                    # Output: "111"
print("\t", consensus_or(["110", "111", "100"]))                    # Output: "111"
print("\t", consensus_or(["100", "000", "110"]))                    # Output: "110"


"""
# [💪 Challenge ✨5.5] Confidence Score ===============================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Confidence = (number of '1's in consensus_mask) / total positions
        Score ranges from 0.0 to 1.0 (how confident the group is in full agreement)
    Function Signature:
        def confidence_score(binary_str_list: List[str]) -> float:
            pass
    Example:
        Input: ["111", "101", "111"]                                # Output: 0.67
# ----------------------------------------------------------------------------------------------------------------------
"""
def confidence_score(binary_str_list: List[str]) -> float:
    agree_count = 0
    for i in range(len(binary_str_list[0])):                        # Number of characters in the string (each bit position).
        one_count = 0
        for j in range(len(binary_str_list)):                       # Number of elements in the list (each binary string).
            one_count += 1 if binary_str_list[j][i] == '1' else 0
        if one_count == 0 or one_count == len(binary_str_list):     # Full agreement on bit.
            agree_count += 1 
    return round(agree_count / len(binary_str_list[0]), 2)

print("\n[💪 Challenge ✨5.5] Confidence Score -------------------------------------------")
print("\t", confidence_score(["111", "101", "111"]))                # Output: 0.67  ← Agree = 2/3
print("\t", confidence_score(["111", "111", "111"]))                # Output: 1.0   ← All agree = 3/3 (Full confidence)
print("\t", confidence_score(["110", "111", "100"]))                # Output: 0.33  ← Agree = 1/3
print("\t", confidence_score(["1010", "1011", "1010"]))             # Output: 0.75  ← Agree = 3/4 (All agree except last bit)


"""
# [💪 Challenge ✨5.6] Consensus Analysis =============================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: A combined function that returns both the consensus mask (where all strings agree at a position) and the confidence score (ratio of agreement positions to total).
    Function Signature:
        def consensus_analysis(binary_str_list: List[str]) -> Tuple[str, float]:
            pass
    Example:
        Input: ["1010", "1011", "1010"]                             # Output: ("1110", 0.75)
    Rules:
    Hints:
# ----------------------------------------------------------------------------------------------------------------------
"""
def consensus_analysis(binary_str_list: List[str]) -> Tuple[str, float]:
    consensus_mask = ""
    agree_count = 0
    for i in range(len(binary_str_list[0])):                        # Number of characters in the string (each bit position).
        one_count = sum(1 for binary_str in binary_str_list if binary_str[i] == '1')
        if one_count == 0 or one_count == len(binary_str_list):     # Full agreement on bit.
            consensus_mask += '1'
            agree_count += 1
        else:
            consensus_mask += '0'                                   # Disagreement
    confidence_score = round(agree_count / len(binary_str_list[0]), 2)
    return consensus_mask, confidence_score

print("\n[💪 Challenge ✨5.6] Consensus Analysis -----------------------------------------")
print("\t", consensus_analysis(["1010", "1011", "1010"]))           # Output: ("1110", 0.75)


"""
# [💪 Challenge ✨5.7] Consensus Report ===============================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Let’s extend our report to include:
            1. Consensus Mask (all-agree): '1' if everyone agrees on that bit
            2. Consensus OR (any-one-says-1): '1' if at least one string has a 1
            3. Disagreement Map: '1' where there is partial agreement (some 0’s and some 1’s)
            4. Confidence Score: fraction of positions with full agreement
    Function Signature:
        class ConsensusReport(NamedTuple):
            consensus_mask: str
            consensus_or: str
            disagreement_map: str
            confidence_score: float

        def consensus_report(binary_str_list: List[str]) -> ConsensusReport:
            pass
    Example:
        consensus_report(["1010", "1011", "1000", "1010"])          # Output: 7
# ----------------------------------------------------------------------------------------------------------------------
"""
class ConsensusReport(NamedTuple):
    consensus_mask: str
    consensus_or: str
    disagreement_map: str
    confidence_score: float

def consensus_report(binary_str_list: List[str]) -> ConsensusReport:
    mask_all = []
    mask_any = []
    mask_disagree = []
    agree_count = 0

    for i in range(len(binary_str_list[0])):                        # Number of characters in the string (each bit position).
        one_count = sum(1 for binary_str in binary_str_list if binary_str[i] == '1')

        # Consensus Mask: everyone agrees on '1'
        mask_all.append('1' if one_count == len(binary_str_list) else '0')

        # Consensus OR: at least one '1'
        mask_any.append('1' if one_count >= 1 else '0')

        # Disagreement: some say '1' and some say '0'
        mask_disagree.append('1' if 0 < one_count < len(binary_str_list) else '0')

        # Count full-agreement positions (either all 1’s or all 0’s)
        agree_count += 1 if one_count == 0 or one_count == len(binary_str_list) else 0
    
    consensus_mask      = ''.join(mask_all)                                 # Mask All-Agree: Positions where all bits are 1
    consensus_or        = ''.join(mask_any)                                 # Mask Anyone-1: Positions where at least one bit is 1
    disagreement_map    = ''.join(mask_disagree)                            # Disagreement Map: Positions with mixed bits
    confidence_score    = round(agree_count / len(binary_str_list[0]), 2)   # Confidence Score: Proportion of positions with full (all-0 or all-1) agreement

    return ConsensusReport(
        consensus_mask=consensus_mask,
        consensus_or=consensus_or,
        disagreement_map=disagreement_map,
        confidence_score=confidence_score
    )

print("\n[💪 Challenge ✨5.7] Consensus Report -------------------------------------------")
print("\t", consensus_report(["1010", "1011", "1000", "1010"]))     # Output: ConsensusReport(consensus_mask='1000', consensus_or='1011', disagreement_map='0011', confidence_score=0.5)


"""
# [💪 Challenge ✨]  ==================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem: 
    Function Signature:
        def 
            pass
    Example:
        find_word("I love learning Python", "learning")             # Output: 7
    Rules:
    Hints:
# ----------------------------------------------------------------------------------------------------------------------
"""
# def
#     pass

# print("\n[💪 Challenge ✨1.1] Find Word In Sentence --------------------------------------")
# print("\n[💪 Challenge ✨] ---------------------------------------------------------------")
# print("\t", find_word("I love learning Python", "learning"))        # Output: 7
# print("\t", )# Output: 