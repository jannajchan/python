"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 Here's an easy challenge to help you practice string indexing and searching.
# ----------------------------------------------------------------------------------------------------------------------

# [💪 Challenge ✨1.1] Find word in sentence ==========================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Write a function that returns the index of the first occurrence of a word in a sentence.
    Function Signature:
        def find_word(sentence: str, word: str) -> int:
            pass
    Example:
        find_word("I love learning Python", "learning") → 7
        find_word("Python is fun", "Java") → -1
        find_word("apple banana cherry", "banana") → 6
    Hints: 
        - Use slicing like sentence[i:i+len(word)]
        - Loop from i = 0 to len(sentence) - len(word) + 1
# ----------------------------------------------------------------------------------------------------------------------
"""
def find_word(sentence: str, word: str) -> int:
    if not word: # Handling the edge case where word is an empty string.
        return 0
    
    for i in range(len(sentence) - len(word) + 1): # This ensures the window you're checking (sentence[i : i + len(word)]) never goes out of bounds.
        if sentence[i : i + len(word)] == word: # You're checking slices of the sentence that match the length of word, and comparing them directly.
            return i
    return -1

print("[💪 Challenge ✨1.1] Find word in sentence --------------------------------------")
print("\t", find_word("I love learning Python", "learning"))        # Output: 7
print("\t", find_word("Python is fun", "Java"))                     # Output: -1
print("\t", find_word("apple banana cherry", "banana"))             # Output: 6


"""
# [💪 Challenge ✨1.2] Case-insensitive word search with whole word match =============================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Write a function that finds the index of the first occurrence of a word in a sentence, but:
        - It should ignore case (case-insensitive).
        - It should only match whole words (not substrings inside other words).
    Function Signature:
        def find_whole_word(sentence: str, word: str) -> int:
            pass
    Example:
        find_whole_word("I love Python", "python")      # ➞ 7
        find_whole_word("She sells seashells", "sell")  # ➞ -1  (it's not a full word)
        find_whole_word("Go big or go home", "GO")      # ➞ 0
    Hints: 
        1. Use str.lower() to make both the sentence and word lowercase.
        2. Use .split() to break the sentence into words.
        3. Loop over the words and keep track of the character index you're at.
        4. Only return the index if a word matches exactly.
# ----------------------------------------------------------------------------------------------------------------------
"""
# [My version] --------------------------------------------------
# What your code does well:
#   ✅ Handles an empty word case.
#   ✅ Splits the sentence into words with split().
#   ✅ Compares words case-insensitively.
#   ✅ Computes the correct starting index in the original sentence.
#   ✅ Returns -1 if no match is found.
def find_whole_word_myVersion(sentence: str, word: str) -> int:
    if not word:
        return 0
    
    wordList = sentence.split()
    for i, value in enumerate(wordList):
        if value.lower() == word.lower():
            index = 0
            for j in range(0, i):
                index += len(wordList[j]) + 1
            return index
    return -1

# [Cleaner version] --------------------------------------------------
# You could slightly simplify the index calculation using a generator expression
def find_whole_word(sentence: str, word: str) -> int: #👏😎
    if not word:
        return 0
    
    wordList = sentence.split()
    for i, value in enumerate(wordList):
        if value.lower() == word.lower():
            return sum(len(w) + 1 for w in wordList[:i]) # +1 accounts for the space
    return -1

print("[💪 Challenge ✨1.2] Find whole word --------------------------------------------")
print("\t", find_whole_word("I love Python", "python"))             # Output: 7
print("\t", find_whole_word("She sells seashells", "sell"))         # Output: -1 (It's not a full word.)
print("\t", find_whole_word("Go big or go home", "GO"))             # Output: 0
print("\t", find_whole_word("This is a test string", "test"))       # Output: 10


"""
# [💪 Challenge ✨1.3] Find all whole word occurrences ================================================================ *** I got different output from ChatGPT and still couldn't find solution.
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Write a function that returns a list of all starting indices where a whole word occurs in a sentence.
    Requirements:
        - Match full words only (not substrings).
        - Ignore case sensitivity.
        - Return a list of indices where the word starts in the sentence.
        - If the word does not appear, return an empty list.
    Function Signature:
        def find_all_whole_word(sentence: str, word: str) -> List[int]:
            pass
    Example:
        find_all_whole_word("The cat sat on the catmat with another cat.", "cat")
        # Output: [4, 19, 41]  ← positions where the word "cat" appears as a full word
# ----------------------------------------------------------------------------------------------------------------------
"""
#import string
import re
from typing import List

# def find_all_whole_word(sentence: str, word: str) -> List[int]: # Not done !!
#     if not word:
#         return [0]
#     outputList = []
#     current_index = 0
#     words = sentence.split()
#     for value in words:
#         # Strip punctuation like commas or periods
#         cleaned = value.strip(string.punctuation)
#         if cleaned.lower() == word.lower():
#             outputList.append(current_index)
#         current_index += len(value) + 1  # includes the space after the word
#     return outputList
    # -------------------------------------------------------------------------------------------------------------------------------------------------------
    # | 🚨 The issue: 🚨                                                                                                                                   |
    # | That removes punctuation from each word, but your index tracking (current_index) uses the original uncleaned word, including punctuation.           |
    # | This causes misaligned character positions when:                                                                                                    |
    # | - Words have trailing punctuation (like "CAT!", "cat.", "cat,")                                                                                     |
    # | - You clean them before comparing, but still use the original length for indexing                                                                   |
    # |                                                                                                                                                     |
    # | 🔧 Fix the root problem: 🔧                                                                                                                        |
    # | To get accurate indices for whole words (case-insensitive, punctuation-safe), use regular expressions with \b word boundaries and re.IGNORECASE.    |
    # | That way you:                                                                                                                                       |
    # | - Avoid manual string splitting                                                                                                                     |
    # | - Automatically handle punctuation                                                                                                                  |
    # | - Get correct character indices directly from matches                                                                                               |
    # -------------------------------------------------------------------------------------------------------------------------------------------------------

# def find_all_whole_word(sentence: str, word: str) -> List[int]: # Not done !!
#     if not word:
#         return [0]
#     pattern = r'\b' + re.escape(word) + r'\b'
#     return [match.start() for match in re.finditer(pattern, sentence, flags=re.IGNORECASE)]
    # -------------------------------------------------------------------------------------------------------------------------------------------------------
    # | 🧠 What You Expected: 🧠                                                                                                                           |
    # | - The word "cat" is immediately followed by a comma: "cat,"                                                                                         |
    # | - So "cat" isn't a full word match (should not be counted).                                                                                         |
    # | - You expected: []                                                                                                                                  |
    # |                                                                                                                                                     |
    # | 🤔 But What Actually Happened? 🤔                                                                                                                  |
    # | - The \b word boundary in regex matches between a \w (word char) and a \W (non-word char).                                                          |
    # | - A comma , is a non-word character, so this still counts as a word boundary.                                                                       |
    # | So:                                                                                                                                                 |
    # | - "cat," does match \bcat\b because:                                                                                                                |
    # |     - \b before 'c' is valid (preceded by space)                                                                                                    |
    # |     - \b after 't' is valid (followed by ,, which is non-word)                                                                                      |
    # | - This is why the regex matches and returns [4]                                                                                                     |
    # -------------------------------------------------------------------------------------------------------------------------------------------------------

def find_all_whole_word(sentence: str, word: str) -> List[int]: # Not done !!
    if not word:
        return [0]
    # This ensures exact word match surrounded by space, start, end, or punctuation
    pattern = r'(?<!\w)' + re.escape(word) + r'(?!\w)'
    return [match.start() for match in re.finditer(pattern, sentence, flags=re.IGNORECASE)]
    # -------------------------------------------------------------------------------------------------------------------------------------------------------
    # | 🚩 If You Want Stricter Word Matching (Only Surrounded by Space or Sentence Boundaries): 🚩                                                        |
    # | You need to modify your pattern to match:                                                                                                           |
    # | - Start of string or space                                                                                                                          |
    # | - then the word                                                                                                                                     |
    # | - then space or end of string                                                                                                                       |
    # |     ------------------------------------------------------                                                                                          |
    # |     | pattern = r'(?<!\w)' + re.escape(word) + r'(?!\w)' |                                                                                          |
    # |     ------------------------------------------------------                                                                                          |
    # | This uses negative lookbehind and negative lookahead to ensure that:                                                                                |
    # | - The character before is NOT a word character (i.e., start or space)                                                                               |
    # | - The character after is NOT a word character (i.e., end or space)                                                                                  |
    # |                                                                                                                                                     |
    # | 🤯 But it still got output: [4] ❌ not [] ... Here's what's going on:                                                                              |
    # | - \w includes: A-Z, a-z, 0-9, and _ (underscore)                                                                                                    |
    # | - (?<!\w) checks the character before the match is not a word character.                                                                            |
    # | - cat,:                                                                                                                                             |
    # |     🔹 Before 'c' is a space → ✔️ passes (?<!\w)                                                                                                   |
    # |     🔹 After 't' is a comma  → comma is not a word character → ✔️ passes (?!\w)                                                                    |
    # |   So this pattern still matches "cat," → because a comma is not a word character.                                                                   |
    # |                                                                                                                                                     |
    # | 🛠️ How to Make It Work Exactly As You Want (Whole Words Only) 🛠️                                                                                   |
    # | If you only want to match "cat" as a whole word surrounded by actual spaces or punctuation that forms real word boundaries                          |
    # | — and not things like cat, — you'll need a stricter custom pattern.                                                                                 |
    # -------------------------------------------------------------------------------------------------------------------------------------------------------

print("[💪 Challenge ✨1.3.1] Find all whole word --------------------------------------")
print("\t", find_all_whole_word("The cat sat on the catmat with another cat.", "cat"))                          # Output: [4, 39]
print("\t", find_all_whole_word("The cat sat on the CAT, a black cat.", "cat"))                                 # Output: [4, 19, 32]
print("\t", find_all_whole_word("Is it a cat? Yes, a CAT!", "cat"))     # ⇐ Sentence with more punctuation      # Output: [8, 20]
print("\t", find_all_whole_word("The cat,the other.", "cat"))           # ⇐ Sentence with no space after        # Output: [4] ❌ []
print("\t", find_all_whole_word("This is the cat that you like, the black cat sitting on the catmat.", "cat"))  # Output: [12, 41]
                                #         10        20        30        40        50        60        70
                                #01234567890123456789012345678901234567890123456789012345678901234567890

import re
from typing import List

# def find_all_substring(sentence: str, word: str) -> List[int]:
#     if not word:
#         return [0]
#     outputList = []
#     pattern = re.escape(word)
#     for match in re.finditer(pattern, sentence.lower()): # ⇐ The discrepancy
#         outputList.append(match.start())
#     return outputList
    # -------------------------------------------------------------------------------------------------------------------------------------------------------
    # | 🚨 The issue: The discrepancy in output 🚨                                                                                                         |
    # | ... comes from the use of .lower() applied only to the sentence, but not updating the original string index accordingly.                            |
    # |                                                                                                                                                     |
    # | You're running the regex on sentence.lower() and collecting match.start() — which is the index in the lowercase version of the string.              |
    # | But if the original sentence has a different number of uppercase/lowercase letters, or different byte lengths for non-ASCII characters,             |
    # | the indices may not match exactly between sentence and sentence.lower().                                                                            |
    # |                                                                                                                                                     |
    # | To ensure accurate indexing with the original string, you should use re.IGNORECASE.                                                                 |
    # | Instead of lowercasing the sentence, keep the original and pass a flag.                                                                             |
    # | Now you’ll get accurate positions from the original sentence, and the outputs will match the real string.                                           |
    # -------------------------------------------------------------------------------------------------------------------------------------------------------

def find_all_substring(sentence: str, word: str) -> List[int]:
    if not word:
        return [0]
    
    outputList = []
    pattern = re.escape(word)
    for match in re.finditer(pattern, sentence, flags=re.IGNORECASE):
        outputList.append(match.start())
    return outputList

print("[💪 Challenge ✨1.3.2] Find all substring ---------------------------------------")
print("\t", find_all_substring("The cat sat on the catmat with another cat.", "cat"))                           # Output: [4, 19, 39]
print("\t", find_all_substring("The cat sat on the CAT, a black cat.", "cat"))                                  # Output: [4, 19, 32]
print("\t", find_all_substring("Is it a cat? Yes, a CAT!", "cat"))     # ⇐ Sentence with more punctuation       # Output: [8, 20]
print("\t", find_all_substring("The cat,the other.", "cat"))           # ⇐ Sentence with no space after         # Output: [4]
print("\t", find_all_substring("This is the cat that you like, the black cat sitting on the catmat.", "cat"))   # Output: [12, 41, 60]
                               #         10        20        30        40        50        60        70
                               #01234567890123456789012345678901234567890123456789012345678901234567890


"""
# [💪 Challenge ✨2.1] First vowel index ==============================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Write a function that returns the index of the first vowel (a, e, i, o, u) in a given string. If no vowels found, return -1.
    Function Signature:
        def first_vowel_index(s: str) -> int:
            pass
    Example:
        first_vowel_index("strength") → 3
        first_vowel_index("rhythm") → -1
# ----------------------------------------------------------------------------------------------------------------------
"""
def first_vowel_index(s: str) -> int:
    if not s:
        return -1
    
    vowel = "aeiou"
    for i, char in enumerate(s):
        if char in vowel:
            return i
    return -1

print("[💪 Challenge ✨2.1] First vowel index ------------------------------------------")
print("\t", first_vowel_index("strength"))                          # Output: 3
print("\t", first_vowel_index("rhythm"))                            # Output: -1
print("\t", first_vowel_index("animal"))                            # Output: 0


"""
# [💪 Challenge ✨2.2] Count occurrences of a substring ===============================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Count how many times a substring appears in a string, case-insensitive.
    Function Signature:
        def count_occurrences(text: str, word: str) -> int:
            pass
    Example:
        count_occurrences("The dog chased the Dog", "dog") → 2
# ----------------------------------------------------------------------------------------------------------------------
"""
def count_occurrences(text: str, word: str) -> int: #case-insensitive
    if not word:
        return 0
    
    count = 0
    for i in range(len(text) - len(word) + 1):
        if text[i : i + len(word)].lower() == word.lower():
            count += 1
    return count


print("[💪 Challenge ✨2.2] Count occurrences of a substring ---------------------------")
print("\t", count_occurrences("The dog chased the Dog", "dog"))                                             # Output: 2
print("\t", count_occurrences("This man is sitting on his chair, listening to his music record.", "is"))    # Output: 5


"""
# [💪 Challenge ✨2.3] Find all capital letters =======================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Return a list of indexes where capital letters appear in the input string.
    Function Signature:
        def find_capitals(s: str) -> List[int]:
            pass
    Example:
        find_capitals("HeLLo World") → [0, 2, 3, 6]
# ----------------------------------------------------------------------------------------------------------------------
"""
def find_capitals(s: str) -> List[int]:
    if not s:
        return []
    
    outputList = []
    for i, char in enumerate(s):
        if char.isupper():
            outputList.append(i)
    return outputList


print("[💪 Challenge ✨2.3] Find all capital letters -----------------------------------")
print("\t", find_capitals("HeLLo World"))                           # Output: [0, 2, 3, 6]
print("\t", find_capitals("Hello World"))                           # Output: [0, 6]
print("\t", find_capitals("PYTHON"))                                # Output: [0, 1, 2, 3, 4, 5]
print("\t", find_capitals("lowercase"))                             # Output: []
print("\t", find_capitals(""))                                      # Output: []


"""
# [💪 Challenge ✨2.4] Reverse words in sentence ======================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Reverse each word in the sentence, keeping the original word order.
    Function Signature:
        def reverse_words(sentence: str) -> str:
            pass
    Example:
        reverse_words("hello world") → "olleh dlrow"
# ----------------------------------------------------------------------------------------------------------------------
"""
# def reverse_words(sentence: str) -> str:
#     if not sentence:
#         return ""
#     s = sentence.split()
#     output = ""
#     for i in range(len(s)):
#         if i > 0:
#             output += " "
#         output += s[i][::-1]
#     return output

def reverse_words(sentence: str) -> str:
    if not sentence:
        return ""
    return ' '.join(word[::-1] for word in sentence.split()) # Alternatively, you can simplify the loop using a one-liner.

print("[💪 Challenge ✨2.4] Reverse words in sentence ----------------------------------")
print("\t", reverse_words("hello world"))                           # Output: olleh dlrow


"""
# [💪 Challenge ✨2.5] Replace every second occurrence ================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Replace every 2nd occurrence of a character with "*".
    Function Signature:
        def mask_second_occurrence(s: str, target: str) -> str:
            pass
    Example:
        mask_second_occurrence("banana", "a") → "ban*na"
# ----------------------------------------------------------------------------------------------------------------------
"""
# def mask_second_occurrence(s: str, target: str) -> str:
#     if not target:
#         return s    
#     replaceTxt = ""
#     count = 0
#     for i in range(len(s) - len(target) + 1):
#         if s[i : i + len(target)].lower() == target.lower():
#             count += 1
#             if count == 2:
#                 replaceTxt += "*"
#         replaceTxt += s[i]
#     return replaceTxt
    # ------------------------------------------------------------------------------------------------------------------------
    # | ❌ The current version incorrectly appends overlapping characters and doesn’t fully handle non-matching slices. ❌  |
    # | Problem:                                                                                                             |
    # | - It checks for substring target in slices.                                                                          |
    # | - It appends s[i] even when it's part of a substring match — causing duplicated characters.                          |
    # | - It doesn't advance the index past matched substrings.                                                              |
    # | Let's walk through the fix:                                                                                          |
    # ------------------------------------------------------------------------------------------------------------------------

def mask_second_occurrence(s: str, target: str) -> str:
    if not target:
        return s
    result = ""
    i = 0
    count = 0
    while i < len(s):
        if s[i : i+len(target)].lower() == target.lower():
            count += 1
            if count == 2:
                result += "*"
            else:
                result += s[i : i+len(target)]
            i += len(target)
        else:
            result += s[i]
            i += 1
    return result

print("[💪 Challenge ✨2.1] Replace every second occurrence ----------------------------")
print("\t", mask_second_occurrence("banana", "a"))                  # Output: "ban*na"
print("\t", mask_second_occurrence("hahaha", "ha"))                 # Output: "ha*ha"


# Here's a slightly harder version of each of your challenges — still beginner-friendly but pushes your logic and understanding a bit further:
"""
# [💪 Challenge ✨3.1] Second vowel index (Extended) ==================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Challenge:
        Find the index of the second vowel in a string. Return -1 if there are fewer than two vowels.
    Function Signature:
        def second_vowel_index(s: str) -> int:
            pass
    Example:
        second_vowel_index("apple") → 4
        second_vowel_index("why") → -1
# ----------------------------------------------------------------------------------------------------------------------
"""
def second_vowel_index(s: str) -> int:
    if not s:
        return -1
    
    vowel = "aeiou"
    count = 0
    for i, char in enumerate(s):
        if char.lower() in vowel:
            count += 1
            if count == 2:
                return i
    return -1

print("[💪 Challenge ✨3.1] Second vowel index (Extended) ------------------------------")
print("\t", second_vowel_index("apple"))                            # Output: 4
print("\t", second_vowel_index("why"))                              # Output: -1


"""
# [💪 Challenge ✨3.2] Count word occurrences (Whole word only) =======================================================
# ----------------------------------------------------------------------------------------------------------------------
    Challenge:
        Count how many times the exact word appears in a sentence, case-insensitive.
        It must be a whole word, not part of another.
    Function Signature:
        def count_whole_word_occurrences(text: str, word: str) -> int:
            pass
    Example:
        count_whole_word_occurrences("The cat sat on the catmat with another cat.", "cat") → 2
# ----------------------------------------------------------------------------------------------------------------------
"""
def count_whole_word_occurrences(text: str, word: str) -> int:
    import string
    count = 0
    for w in text.split():
        w_clean = w.strip(string.punctuation)
        if w_clean.lower() == word.lower():
            count += 1
    return count

print("[💪 Challenge ✨3.2] Count word occurrences (Whole word only) -------------------")
print("\t", count_whole_word_occurrences("The cat sat on the catmat with another cat.", "cat"))     # Output: 2


"""
# [💪 Challenge ✨3.3] Find capitalized words (Not just letters) ======================================================
# ----------------------------------------------------------------------------------------------------------------------
    Challenge:
        Return a list of all full words that start with a capital letter.
    Function Signature:
        def find_capitalized_words(s: str) -> List[str]:
            pass
    Example:
        find_capitalized_words("Today is a Great Day in Rome") → ['Today', 'Great', 'Day', 'Rome']
# ----------------------------------------------------------------------------------------------------------------------
"""
# def find_capitalized_words(s: str) -> List[str]:
#     sList = s.split()
#     capitalizedList = []
#     for i in range(len(sList)):
#         if sList[i][0].isupper():
#             capitalizedList.append(sList[i])
#     return capitalizedList
    # -------------------------------------------------------------------
    # | The code works perfectly. But could simplify slightly ...       |
    # -------------------------------------------------------------------

def find_capitalized_words(s: str) -> List[str]:
    return [w for w in s.split() if w[0].isupper()]

print("[💪 Challenge ✨3.3] Find capitalized words (Not just letters) ------------------")
print("\t", find_capitalized_words("Today is a Great Day in Rome")) # Output: ['Today', 'Great', 'Day', 'Rome']


"""
# [💪 Challenge ✨3.4] Reverse every Nth word =========================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Challenge:
        Reverse every nth word in a sentence (starting from 1). ⇐ Nth word = The word that is in the Nth position in the sentence (position % n == 0).
    Function Signature:
        def reverse_every_nth(sentence: str, n: int) -> str:
            pass
    Example:
        reverse_every_nth("This is a simple test case", 2) → "This si a elpmis test esac"
            [1] "This"       → stays the same  
            [2] "is"         → reversed to "si"  
            [3] "a"          → stays the same  
            [4] "simple"     → reversed to "elpmis"  
            [5] "test"       → stays the same  
            [6] "case"       → reversed to "esac"
# ----------------------------------------------------------------------------------------------------------------------
"""
# def reverse_every_nth(sentence: str, n: int) -> str:
#     sList = sentence.split()
#     outputTxt = ""
#     for i in range(len(sList)):
#         if i > 0:
#             outputTxt += " "
#         if (i + 1) % n == 0:
#             outputTxt += sList[i][::-1]
#         else:
#             outputTxt += sList[i]
#     return outputTxt
    # -------------------------------------------------------------------
    # | You can use " ".join(...) instead of manual string building.    |
    # -------------------------------------------------------------------

def reverse_every_nth(sentence: str, n: int) -> str:
    words = sentence.split()
    for i in range(len(words)):
        if (i + 1) % n == 0:
            words[i] = words[i][::-1]
    return " ".join(words)

print("[💪 Challenge ✨3.4] Reverse every Nth word -------------------------------------")
print("\t", reverse_every_nth("This is a simple test case", 2))     # Output: "This si a elpmis test esac"


"""
# [💪 Challenge ✨3.5] Mask all except first occurrence ===============================================================
# ----------------------------------------------------------------------------------------------------------------------
    Challenge:
        Replace all occurrences of a target (case-insensitive) except the first one with *.
        = replace every occurrence of target after the first with "*", while keeping all other words unchanged.
    Function Signature:
        def mask_except_first(s: str, target: str) -> str:
            pass
    Example:
        mask_except_first("banana banana banana", "banana") → "banana * *"
# ----------------------------------------------------------------------------------------------------------------------
"""
# def mask_except_first(s: str, target: str) -> str:
#     sList = s.split()
#     outputTxt = ""
#     for i in range(len(sList)):
#         if sList[i] == target:
#             if i == 0:
#                 outputTxt += sList[0]
#             else:
#                 outputTxt += " *"
#     return outputTxt
    # ---------------------------------------------------------------------------------------------------------------
    # | 🚨 Issue: 🚨                                                                                               |
    # | - You're comparing each word to the target, but you only preserve the first word if it's a match (i == 0),  |
    # |   not the first occurrence of the target.                                                                   |
    # | - Also, it doesn't keep the rest of the words that don't match.                                             |
    # ---------------------------------------------------------------------------------------------------------------

def mask_except_first(s: str, target: str) -> str:
    wordList = s.split()
    seenFlag = False
    result = []
    for word in wordList:
        if word == target:
            if not seenFlag:
                result.append(word) # Keep the first match
                seenFlag = True     # Mark that we've already seen it
            else:
                result.append("*")  # Replace later matches
        else:
            result.append(word)     # Keep other words unchanged
    return " ".join(result)
    # ---------------------------------------------------------------------------------------------------------------
    # | 🔑 Key Concepts: 🔑                                                                                        |
    # | 1. Splitting the sentence:                                                                                  |
    # |         wordList = s.split()        # This breaks the string into a list of words using spaces.             |
    # | 2. "seenFlag" variable: This boolean tracks whether we've already seen the first occurrence of target.      |
    # | 3. Loop over words: Each word is checked ...                                                                |
    # |     - If it's the target and we haven’t seen it yet → keep it, set seenFlag = True.                         |
    # |     - If it's the target and we have seen it        → replace it with "*".                                  |
    # |     - Otherwise: just keep the word.                                                                        |
    # | 4. Joining words back: After the loop, we use ...                                                           |
    # |         return " ".join(result)     # To rebuild the sentence.                                              |
    # |                                                                                                             |
    # | 👍 What it handles well: 👍                                                                                |
    # | - It preserves word order.                                                                                  |
    # | - It preserves case sensitivity.                                                                            |
    # | - It replaces only exact matches (not partial matches or substrings).                                       |
    # ---------------------------------------------------------------------------------------------------------------

print("[💪 Challenge ✨3.5] Mask all except first occurrence ---------------------------")
print("\t", mask_except_first("banana banana banana", "banana"))            # Output: "banana * *"
print("\t", mask_except_first("apple banana apple grape apple", "apple"))   # Output: "apple banana * grape *"


"""
# [💪 Challenge ✨4] Mask emails in text ==============================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Here’s a slightly trickier challenge involving regex and string indexing:
    Problem:
        Given a sentence, mask all email addresses by replacing everything between the first character and the @ sign with "***".
    Example:
        Input: "Please contact john.doe@example.com or jane99@mail.org for details."
        Output: "Please contact j***@example.com or j***@mail.org for details."
    Rules:
        - Keep the first letter of the email.
        - Replace the characters before @ with "***" (after the first letter).
        - Keep everything after @ untouched.
    Hints:
        - Use re.findall() or re.sub() with a regular expression to identify email patterns.
        - You may capture groups in regex like: ([a-zA-Z0-9._%+-])([a-zA-Z0-9._%+-]*?)@([\w.-]+\.\w+)
# ----------------------------------------------------------------------------------------------------------------------
"""
# def mask_emails_in_text_myVersion(text: str) -> str:
#     wordList = text.split()
#     result = []
#     for word in wordList:
#         if "@" in word:
#             emailList = word.split("@")
#             result.append(emailList[0][0] + "***@" + emailList[1])
#         else:
#             result.append(word)     # Keep other words unchanged
#     return " ".join(result)
    # ---------------------------------------------------------------------------------------------------------------------------
    # | 🚨 At a glance, seem to produce the same visible output 🚨                                                             |
    # | Both "mask_emails_in_text_myVersion" and "mask_emails_in_text_regexVersion" for basic test cases like:                  |
    # |         "Please contact john@example.com and jane@mail.com."                                                            |
    # | Both would yield: "Please contact j***@example.com and j***@mail.com."                                                  |
    # |                                                                                                                         |
    # | However, the key differences show up when emails have punctuation attached to them or when formatting gets trickier.    |
    # | Here's a breakdown ...                                                                                                  |
    # |                                                                                                                         |
    # | 🔴 Limitations: 🔴                                                                                                     |
    # | - It uses split() on spaces, so it fails to isolate punctuation:                                                        |
    # |         "Email: john@example.com!"      ⇐ ❌ Wrong, includes the '!' in the domain                                     |
    # |         # Result: 'j***@example.com!'                                                                                   |
    # | - Fails if the word is something like:                                                                                  |
    # |         "john@example.com,"             ⇐ ❌ Wrong, comma gets mixed into the domain                                   |
    # |         # Result: 'j***@example.com,'                                                                                   |
    # |                                                                                                                         |
    # | 🚨 Issue: 🚨                                                                                                           |
    # |     It doesn't remove or preserve trailing punctuation like commas or exclamation marks that are attached to the email  |
    # | (e.g. example.com, or org!). So the masked email ends up with punctuation on the domain part, which could cause         |
    # | unexpected results.                                                                                                     |
    # |                                                                                                                         |
    # | 🔧 How to Improve: 🔧 You can use regular expressions to ...                                                           |
    # |     - Match email patterns safely (even with punctuation).                                                              |
    # |     - Use capture groups to isolate parts of the email.                                                                 |
    # ---------------------------------------------------------------------------------------------------------------------------

import re

def mask_emails_in_text_regexVersion(text: str) -> str:
    pattern = r'([a-zA-Z0-9._%+-])([a-zA-Z0-9._%+-]*?)@([\w.-]+\.\w+)'
    def masker(match):
        return f"{match.group(1)}***@{match.group(3)}"
    return re.sub(pattern, masker, text)
    # ---------------------------------------------------------------------------------------------------------------------------
    # | 🚩 Regex Version: 🚩                                                                                                   |
    # | Advantages:                                                                                                             |
    # |     - Matches the email structure only, excluding trailing punctuation.                                                 |
    # |     - Works even if email is not separated by spaces or is inside HTML tags, etc.                                       |
    # |     - Handles edge cases like:                                                                                          |
    # |         - "john@example.com,"                                                                                           |
    # |         - "contact us at john@example.com!"                                                                             |
    # |         - "hello(john@example.com)"                                                                                     |
    # | 🔬 Test Case Comparison: 🔬                                                                                            |
    # |     text = "Send it to john@example.com, jane@mail.org!"                                                                |
    # | Output:                                                                                                                 |
    # |     - Yours: Send it to j***@example.com, j***@mail.org!    # example.com, → the comma is part of domain                |
    # |     - Regex: Send it to j***@example.com, j***@mail.org!    # example.com is correctly extracted                        |
    # | But under the hood:                                                                                                     |
    # |     - Yours: domain becomes "example.com,"                                                                              |
    # |     - Regex: domain stays "example.com"                                                                                 |
    # ---------------------------------------------------------------------------------------------------------------------------

print("[💪 Challenge ✨4] Mask emails in text ------------------------------------------")
print("\t", mask_emails_in_text_regexVersion("Please contact john.doe@example.com or jane99@mail.org for details."))    # Output: "Please contact j***@example.com or j***@mail.org for details."
print("\t", mask_emails_in_text_regexVersion("Please contact john.doe@example.com, or jane99@mail.org!"))               # Output: "Please contact j***@example.com, or j***@mail.org!"


"""
# [💪 Challenge ✨5.1] Find all palindromic substrings ================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Write a function that returns all substrings of a given string that are palindromes (read the same forwards and backwards) and have length ≥ 2.
    Function Signature:
        def find_palindromes(s: str) -> List[str]:
            pass
    Example:
        find_palindromes("racecar madam level")                     # Possible Output: ['racecar', 'cec', 'madam', 'ada', 'level', 'eve']
# ----------------------------------------------------------------------------------------------------------------------
"""
def find_palindromes(s: str) -> List[str]:
    pass

print("[💪 Challenge ✨5.1] Find all palindromic substrings ----------------------------")
print("\t", find_palindromes("racecar madam level"))                # Output: 


"""
# [💪 Challenge ✨5.2] Most frequent word (Case-insensitive) ==========================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Return the most frequently occurring word in a sentence. Ignore punctuation and make it case-insensitive.
    Function Signature:
        def most_frequent_word(text: str) -> str:
            pass
    Example:
        most_frequent_word("Dog cat dog, dog. cat!")                # Output: "dog"
# ----------------------------------------------------------------------------------------------------------------------
"""
def most_frequent_word(text: str) -> str:
    import string
    cleaned_word = text.lower().strip(string.punctuation) # Strip punctuation like commas or periods
    print(cleaned_word)

print("[💪 Challenge ✨5.2] Most frequent word (Case-insensitive) ----------------------")
print("\t", most_frequent_word("Dog cat dog, dog. cat!"))           # Output: 


"""
# [💪 Challenge ✨5.3] Remove all repeated characters =================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Return a new string with only the first occurrence of each character, preserving order.
    Function Signature:
        def remove_repeats(s: str) -> str:
            pass
    Example:
        remove_repeats("banana")                                    # Output: "ban"
# ----------------------------------------------------------------------------------------------------------------------
"""
def remove_repeats(s: str) -> str:
    pass

print("[💪 Challenge ✨5.3] Remove all repeated characters -----------------------------")
print("\t", remove_repeats("banana"))                               # Output: 


"""
# [💪 Challenge ✨5.4] Find N-th occurrence index =====================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Find the index of the N-th occurrence of a substring in a string.
    Function Signature:
        def find_nth_occurrence(text: str, word: str, n: int) -> int:
            pass
    Example:
        find_nth_occurrence("abc cat dog cat mouse cat", "cat", 3)  # Output: index of third "cat"
# ----------------------------------------------------------------------------------------------------------------------
"""
def find_nth_occurrence(text: str, word: str, n: int) -> int:
    pass

print("[💪 Challenge ✨5.4] Find N-th occurrence index ---------------------------------")
print("\t", find_nth_occurrence("abc cat dog cat mouse cat", "cat", 3))     # Output: 


"""
# [💪 Challenge ✨5.5] Censor words in a list =========================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Given a sentence and a list of "bad" words, replace all full matches with "***".
    Function Signature:
        def censor_words(sentence: str, banned: List[str]) -> str:
            pass
    Example:
        censor_words("This is a bad sentence with dumb words", ["bad", "dumb"])         # Output: "This is a *** sentence with *** words"
# ----------------------------------------------------------------------------------------------------------------------
"""
def censor_words(sentence: str, banned: List[str]) -> str:
    pass

print("[💪 Challenge ✨5.5] Censor words in a list -------------------------------------")
print("\t", censor_words("This is a bad sentence with dumb words", ["bad", "dumb"]))    # Output: 


"""
# [💪 Challenge ✨5.6] Capitalize all first letters ===================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Capitalize the first letter of each word, lower the rest.
    Function Signature:
        def smart_title(text: str) -> str:
            pass
    Example:
        smart_title("tHis is a tItle")                              # Output: "This Is A Title"
# ----------------------------------------------------------------------------------------------------------------------
"""
def smart_title(text: str) -> str:
    pass

print("[💪 Challenge ✨5.6] Capitalize all first letters -------------------------------")
print("\t", smart_title("tHis is a tItle"))                         # Output: 





"""
# [💪 Challenge ✨]  ==================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
    Function Signature:

            pass
    Example:
    Rules:
    Hints:
# ----------------------------------------------------------------------------------------------------------------------
"""
print("[💪 Challenge ✨] ---------------------------------------------------------------")
print("\t", )# Output: 