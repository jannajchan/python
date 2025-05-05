import string
import re
from typing import List

"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 Here's an easy challenge to help you practice string indexing, manipulating and searching.
# ----------------------------------------------------------------------------------------------------------------------

# [💪 Challenge ✨1.1] Find Word In Sentence ==========================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Write a function that returns the index of the first occurrence of a word in a sentence.
    Function Signature:
        def find_word(sentence: str, word: str) -> int:
            pass
    Example:
        find_word("I love learning Python", "learning")             # Output: 7
        find_word("Python is fun", "Java")                          # Output: -1
        find_word("apple banana cherry", "banana")                  # Output: 6
    Hints: 
        - Use slicing like sentence[i:i+len(word)]
        - Loop from i = 0 to len(sentence) - len(word) + 1
# ----------------------------------------------------------------------------------------------------------------------
"""
def find_word(sentence: str, word: str) -> int:
    if not word: # Handling the edge case where word is an empty string.
        return 0
    
    for i in range(len(sentence) - len(word) + 1): # This ensures the window you're checking (sentence[i:i+len(word)]) never goes out of bounds.
        if sentence[i:i+len(word)] == word: # You're checking slices of the sentence that match the length of word, and comparing them directly.
            return i
    return -1

print("\n[💪 Challenge ✨1.1] Find Word In Sentence --------------------------------------")
print("\t", find_word("I love learning Python", "learning"))        # Output: 7
print("\t", find_word("Python is fun", "Java"))                     # Output: -1
print("\t", find_word("apple banana cherry", "banana"))             # Output: 6


"""
# [💪 Challenge ✨1.2] Case-Insensitive Word Search with Whole Word Match =============================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Write a function that finds the index of the first occurrence of a word in a sentence, but:
        - It should ignore case (case-insensitive).
        - It should only match whole words (not substrings inside other words).
    Function Signature:
        def find_whole_word(sentence: str, word: str) -> int:
            pass
    Example:
        find_whole_word("I love Python", "python")                  # Output: 7
        find_whole_word("She sells seashells", "sell")              # Output: -1  (it's not a full word)
        find_whole_word("Go big or go home", "GO")                  # Output: 0
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

print("\n[💪 Challenge ✨1.2] Find Whole Word --------------------------------------------")
print("\t", find_whole_word("I love Python", "python"))             # Output: 7
print("\t", find_whole_word("She sells seashells", "sell"))         # Output: -1 (It's not a full word.)
print("\t", find_whole_word("Go big or go home", "GO"))             # Output: 0
print("\t", find_whole_word("This is a test string", "test"))       # Output: 10


"""
# [💪 Challenge ✨1.3] Find All Whole Word Occurrences ================================================================ *** I got different output from ChatGPT and still couldn't find solution.
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
# def find_all_whole_word(sentence: str, word: str) -> List[int]: # Not done !!
#     if not word:
#         return [0]
#     current_index = 0
#     resultList = []
#     words = sentence.split()
#     for value in words:
#         # Strip punctuation like commas or periods
#         cleaned = value.strip(string.punctuation)
#         if cleaned.lower() == word.lower():
#             resultList.append(current_index)
#         current_index += len(value) + 1  # includes the space after the word
#     return resultList
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

print("\n[💪 Challenge ✨1.3.1] Find All Whole Word --------------------------------------")
print("\t", find_all_whole_word("The cat sat on the catmat with another cat.", "cat"))                          # Output: [4, 39]
print("\t", find_all_whole_word("The cat sat on the CAT, a black cat.", "cat"))                                 # Output: [4, 19, 32]
print("\t", find_all_whole_word("Is it a cat? Yes, a CAT!", "cat"))     # ⇐ Sentence with more punctuation      # Output: [8, 20]
print("\t", find_all_whole_word("The cat,the other.", "cat"))           # ⇐ Sentence with no space after        # Output: [4] ❌ []
print("\t", find_all_whole_word("This is the cat that you like, the black cat sitting on the catmat.", "cat"))  # Output: [12, 41]
                                #         10        20        30        40        50        60        70
                                #01234567890123456789012345678901234567890123456789012345678901234567890

# def find_all_substring(sentence: str, word: str) -> List[int]:
#     if not word:
#         return [0]
#     resultList = []
#     pattern = re.escape(word)
#     for match in re.finditer(pattern, sentence.lower()): # ⇐ The discrepancy
#         resultList.append(match.start())
#     return resultList
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
    
    resultList = []
    pattern = re.escape(word)
    for match in re.finditer(pattern, sentence, flags=re.IGNORECASE):
        resultList.append(match.start())
    return resultList

print("\n[💪 Challenge ✨1.3.2] Find All Substring ---------------------------------------")
print("\t", find_all_substring("The cat sat on the catmat with another cat.", "cat"))                           # Output: [4, 19, 39]
print("\t", find_all_substring("The cat sat on the CAT, a black cat.", "cat"))                                  # Output: [4, 19, 32]
print("\t", find_all_substring("Is it a cat? Yes, a CAT!", "cat"))     # ⇐ Sentence with more punctuation       # Output: [8, 20]
print("\t", find_all_substring("The cat,the other.", "cat"))           # ⇐ Sentence with no space after         # Output: [4]
print("\t", find_all_substring("This is the cat that you like, the black cat sitting on the catmat.", "cat"))   # Output: [12, 41, 60]
                               #         10        20        30        40        50        60        70
                               #01234567890123456789012345678901234567890123456789012345678901234567890


"""
# [💪 Challenge ✨2.1] First Vowel Index ==============================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Write a function that returns the index of the first vowel (a, e, i, o, u) in a given string. If no vowels found, return -1.
    Function Signature:
        def first_vowel_index(s: str) -> int:
            pass
    Example:
        first_vowel_index("strength")                               # Output: 3
        first_vowel_index("rhythm")                                 # Output: -1
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

print("\n[💪 Challenge ✨2.1] First Vowel Index ------------------------------------------")
print("\t", first_vowel_index("strength"))                          # Output: 3
print("\t", first_vowel_index("rhythm"))                            # Output: -1
print("\t", first_vowel_index("animal"))                            # Output: 0


"""
# [💪 Challenge ✨2.2] Count Occurrences of a Substring ===============================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Count how many times a substring appears in a string, case-insensitive.
    Function Signature:
        def count_occurrences(text: str, word: str) -> int:
            pass
    Example:
        count_occurrences("The dog chased the Dog", "dog")          # Output: 2
# ----------------------------------------------------------------------------------------------------------------------
"""
def count_occurrences(text: str, word: str) -> int: #case-insensitive
    if not word:
        return 0
    
    count = 0
    for i in range(len(text) - len(word) + 1):
        if text[i:i+len(word)].lower() == word.lower():
            count += 1
    return count


print("\n[💪 Challenge ✨2.2] Count Occurrences of a Substring ---------------------------")
print("\t", count_occurrences("The dog chased the Dog", "dog"))                                             # Output: 2
print("\t", count_occurrences("This man is sitting on his chair, listening to his music record.", "is"))    # Output: 5


"""
# [💪 Challenge ✨2.3] Find All Capital Letters =======================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Return a list of indexes where capital letters appear in the input string.
    Function Signature:
        def find_capitals(s: str) -> List[int]:
            pass
    Example:
        find_capitals("HeLLo World")                                # Output: [0, 2, 3, 6]
# ----------------------------------------------------------------------------------------------------------------------
"""
def find_capitals(s: str) -> List[int]:
    if not s:
        return []
    
    resultList = []
    for i, char in enumerate(s):
        if char.isupper():
            resultList.append(i)
    return resultList


print("\n[💪 Challenge ✨2.3] Find All Capital Letters -----------------------------------")
print("\t", find_capitals("HeLLo World"))                           # Output: [0, 2, 3, 6]
print("\t", find_capitals("Hello World"))                           # Output: [0, 6]
print("\t", find_capitals("PYTHON"))                                # Output: [0, 1, 2, 3, 4, 5]
print("\t", find_capitals("lowercase"))                             # Output: []
print("\t", find_capitals(""))                                      # Output: []


"""
# [💪 Challenge ✨2.4] Reverse Words in Sentence ======================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Reverse each word in the sentence, keeping the original word order.
    Function Signature:
        def reverse_words(sentence: str) -> str:
            pass
    Example:
        reverse_words("hello world")                                # Output: "olleh dlrow"
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

print("\n[💪 Challenge ✨2.4] Reverse Words in Sentence ----------------------------------")
print("\t", reverse_words("hello world"))                           # Output: olleh dlrow


"""
# [💪 Challenge ✨2.5] Replace Every Second Occurrence ================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Replace every 2nd occurrence of a character with "*".
    Function Signature:
        def mask_second_occurrence(s: str, target: str) -> str:
            pass
    Example:
        mask_second_occurrence("banana", "a")                       # Output: "ban*na"
# ----------------------------------------------------------------------------------------------------------------------
"""
# def mask_second_occurrence(s: str, target: str) -> str:
#     if not target:
#         return s    
#     replaceTxt = ""
#     count = 0
#     for i in range(len(s) - len(target) + 1):
#         if s[i:i+len(target)].lower() == target.lower():
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
    i = 0
    count = 0
    result = ""
    while i < len(s):
        if s[i:i+len(target)].lower() == target.lower():
            count += 1
            if count == 2:
                result += "*"
            else:
                result += s[i:i+len(target)]
            i += len(target)
        else:
            result += s[i]
            i += 1
    return result

print("\n[💪 Challenge ✨2.5] Replace Every Second Occurrence ----------------------------")
print("\t", mask_second_occurrence("banana", "a"))                  # Output: "ban*na"
print("\t", mask_second_occurrence("hahaha", "ha"))                 # Output: "ha*ha"


# Here's a slightly harder version of each of your challenges — still beginner-friendly but pushes your logic and understanding a bit further:
"""
# [💪 Challenge ✨3.1] Second Vowel Index =============================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Challenge: First Vowel Index (Extended)
        Find the index of the second vowel in a string. Return -1 if there are fewer than two vowels.
    Function Signature:
        def second_vowel_index(s: str) -> int:
            pass
    Example:
        second_vowel_index("apple")                                 # Output: 4
        second_vowel_index("why")                                   # Output: -1
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

print("\n[💪 Challenge ✨3.1] Second Vowel Index -----------------------------------------")
print("\t", second_vowel_index("apple"))                            # Output: 4
print("\t", second_vowel_index("why"))                              # Output: -1


"""
# [💪 Challenge ✨3.2] Count Word Occurrences (Whole Word Only) =======================================================
# ----------------------------------------------------------------------------------------------------------------------
    Challenge:
        Count how many times the exact word appears in a sentence, case-insensitive.
        It must be a whole word, not part of another.
    Function Signature:
        def count_whole_word_occurrences(text: str, word: str) -> int:
            pass
    Example:
        count_whole_word_occurrences("The cat sat on the catmat with another cat.", "cat")      # Output: 2
# ----------------------------------------------------------------------------------------------------------------------
"""
def count_whole_word_occurrences(text: str, word: str) -> int:
    count = 0
    for w in text.split():
        w_clean = w.strip(string.punctuation)
        if w_clean.lower() == word.lower():
            count += 1
    return count

print("\n[💪 Challenge ✨3.2] Count Word Occurrences (Whole Word Only) -------------------")
print("\t", count_whole_word_occurrences("The cat sat on the catmat with another cat.", "cat"))     # Output: 2


"""
# [💪 Challenge ✨3.3] Find Capitalized Words (not just letters) ======================================================
# ----------------------------------------------------------------------------------------------------------------------
    Challenge:
        Return a list of all full words that start with a capital letter.
    Function Signature:
        def find_capitalized_words(s: str) -> List[str]:
            pass
    Example:
        find_capitalized_words("Today is a Great Day in Rome")      # Output: ['Today', 'Great', 'Day', 'Rome']
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

print("\n[💪 Challenge ✨3.3] Find Capitalized Words (not just letters) ------------------")
print("\t", find_capitalized_words("Today is a Great Day in Rome")) # Output: ['Today', 'Great', 'Day', 'Rome']


"""
# [💪 Challenge ✨3.4] Reverse Every Nth Word =========================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Challenge:
        Reverse every nth word in a sentence (starting from 1). ⇐ Nth word = The word that is in the Nth position in the sentence (position % n == 0).
    Function Signature:
        def reverse_every_nth(sentence: str, n: int) -> str:
            pass
    Example:
        reverse_every_nth("This is a simple test case", 2)          # Output: "This si a elpmis test esac"
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
#     resultTxt = ""
#     for i in range(len(sList)):
#         if i > 0:
#             resultTxt += " "
#         if (i + 1) % n == 0:
#             resultTxt += sList[i][::-1]
#         else:
#             resultTxt += sList[i]
#     return resultTxt
    # -------------------------------------------------------------------
    # | You can use " ".join(...) instead of manual string building.    |
    # -------------------------------------------------------------------

def reverse_every_nth(sentence: str, n: int) -> str:
    words = sentence.split()
    for i in range(len(words)):
        if (i + 1) % n == 0:
            words[i] = words[i][::-1]
    return " ".join(words)

print("\n[💪 Challenge ✨3.4] Reverse Every Nth Word -------------------------------------")
print("\t", reverse_every_nth("This is a simple test case", 2))     # Output: "This si a elpmis test esac"


"""
# [💪 Challenge ✨3.5] Mask All Except First Occurrence ===============================================================
# ----------------------------------------------------------------------------------------------------------------------
    Challenge:
        Replace all occurrences of a target (case-insensitive) except the first one with *.
        = replace every occurrence of target after the first with "*", while keeping all other words unchanged.
    Function Signature:
        def mask_except_first(s: str, target: str) -> str:
            pass
    Example:
        mask_except_first("banana banana banana", "banana")         # Output: "banana * *"
# ----------------------------------------------------------------------------------------------------------------------
"""
# def mask_except_first(s: str, target: str) -> str:
#     sList = s.split()
#     resultTxt = ""
#     for i in range(len(sList)):
#         if sList[i] == target:
#             if i == 0:
#                 resultTxt += sList[0]
#             else:
#                 resultTxt += " *"
#     return resultTxt
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

print("\n[💪 Challenge ✨3.5] Mask All Except First Occurrence ---------------------------")
print("\t", mask_except_first("banana banana banana", "banana"))            # Output: "banana * *"
print("\t", mask_except_first("apple banana apple grape apple", "apple"))   # Output: "apple banana * grape *"


"""
# [💪 Challenge ✨4] Mask Emails in Text ==============================================================================
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

print("\n[💪 Challenge ✨4] Mask Emails in Text ------------------------------------------")
print("\t", mask_emails_in_text_regexVersion("Please contact john.doe@example.com or jane99@mail.org for details."))    # Output: "Please contact j***@example.com or j***@mail.org for details."
print("\t", mask_emails_in_text_regexVersion("Please contact john.doe@example.com, or jane99@mail.org!"))               # Output: "Please contact j***@example.com, or j***@mail.org!"


"""
# [💪 Challenge ✨5.1] Find All Palindromic Substrings ================================================================
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
# def find_palindromes(s: str) -> List[str]:
#     wordList = re.sub(r'[^a-zA-Z\s]', '', s).lower().strip(string.punctuation).split()
#     palindromeList = []
#     for i in range(len(wordList)):
#         for start in range(len(wordList[i])):
#             for end in range (start + 2, len(wordList[i]) + 1):
#                 sub = wordList[i][start:end]
#                 if sub == sub[::-1] and sub not in palindromeList:
#                     palindromeList.append(sub)
#     return palindromeList                                           # Output: ["racecar", "aceca", "cec", "madam", "ada", "level", "eve"]
    # -----------------------------------------------------------------------------------------------------------------------
    # | 👉 find_palindromes(s: str) 👈                                                                                     |
    # | What you did well:                                                                                                  |
    # |     - Cleaned the input text using regex.                                                                           |
    # |     - Checked substrings within each word for palindromes of length ≥ 2.                                            |
    # |     - Avoided duplicates.                                                                                           |
    # | Suggestions:                                                                                                        |
    # |     - You only find palindromes within words, not across spaces. For example, "abc cba" would miss "bccb".          |
    # -----------------------------------------------------------------------------------------------------------------------

def find_palindromes(s: str) -> List[str]:
    palindromeList = []
    for start in range(len(s)):
        for end in range (start + 2, len(s) + 1):
            sub = s[start:end]
            if sub == sub[::-1] and sub not in palindromeList:
                palindromeList.append(sub)
    return palindromeList
    # -----------------------------------------------------------------------------------------------------------------------
    # | Great improvement — this version of find_palindromes now checks all substrings in the entire string,                |
    # | not just within individual words. That’s a big step forward.                                                        |
    # |                                                                                                                     |
    # | What it's doing well:                                                                                               |
    # |     - It checks all substrings of length ≥ 2.                                                                       |
    # |     - It avoids duplicates with if sub not in palindromeList.                                                       |
    # |     - It detects palindromes regardless of their location or grouping.                                              |
    # | Possible Improvements:                                                                                              |
    # |     1. Case-insensitive comparison (e.g., “Madam” should be counted).                                               |
    # |     2. Ignore non-alphabetic characters or whitespace if needed.                                                    |
    # |     3. Performance optimization: Using a set for palindromeList to avoid linear-time in checks.                     |
    # -----------------------------------------------------------------------------------------------------------------------

def find_palindromes_enhanced(s: str) -> List[str]:
    s = s.lower()
    result = set()
    for start in range(len(s)):
        for end in range(start + 2, len(s) + 1):
            sub = s[start:end]
            if sub == sub[::-1]:
                result.add(sub)
    return list(result)
    # -----------------------------------------------------------------------------------------------------------------------
    # | You now get:                                                                                                        |
    # |     - Case-insensitive matching.                                                                                    |
    # |     - Faster duplicate elimination via set.                                                                         |
    # |     - Cleaner return via list(result).                                                                              |
    # -----------------------------------------------------------------------------------------------------------------------

print("\n[💪 Challenge ✨5.1] Find All Palindromic Substrings ----------------------------")
print("\t", find_palindromes("racecar madam level"))                # Output: ['racecar', 'aceca', 'cec', ' madam ', 'madam', 'ada', 'level', 'eve']
print("\t", find_palindromes_enhanced("racecar madam level"))


"""
# [💪 Challenge ✨5.2] Most Frequent Word (Case-Insensitive) ==========================================================
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
    wordList = re.sub(r'[^a-zA-Z\s]', '', text).lower().strip(string.punctuation).split()
    freqDict = {}
    for word in wordList:
        if word not in freqDict:
            freqDict[word] = 1
        else:
            freqDict[word] += 1
    return max(freqDict, key=freqDict.get)
    # ---------------------------------------------------------------------------------------------------
    # | 👉 most_frequent_word(text: str) 👈                                                            |
    # | Clean and correct.                                                                              |
    # | - You’re stripping punctuation and using .lower()—great.                                        |
    # | - Consider using collections.Counter for shorter code, but yours is totally fine and explicit.  |
    # ---------------------------------------------------------------------------------------------------

print("\n[💪 Challenge ✨5.2] Most Frequent Word (Case-Insensitive) ----------------------")
print("\t", most_frequent_word("Dog cat dog, dog. cat!"))           # Output: "dog"


"""
# [💪 Challenge ✨5.3] Remove All Repeated Characters =================================================================
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
# def remove_repeats(s: str) -> str:
#     if not s:
#         return ""
#     unique = ""
#     for char in s:
#         if char not in unique:
#             unique += char
#     return unique
    # -------------------------------------------------------
    # | 👉 remove_repeats(s: str) 👈                       |
    # | This works, but note:                               |
    # |     - Order is preserved.                           |
    # |     - It’s case-sensitive ("Aa" → "Aa", not "A").   |
    # -------------------------------------------------------

def remove_repeats(s: str) -> str:
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

print("\n[💪 Challenge ✨5.3] Remove All Repeated Characters -----------------------------")
print("\t", remove_repeats("banana"))                               # Output: "ban"


"""
# [💪 Challenge ✨5.4] Find N-th Occurrence Index =====================================================================
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
    count = 0
    for i in range(len(text) - len(word) + 1):
        if word.lower() == text[i:i+len(word)].lower():
            count += 1
        if count == n:
            return i
    return -1

print("\n[💪 Challenge ✨5.4] Find N-th Occurrence Index ---------------------------------")
print("\t", find_nth_occurrence("abc cat dog cat mouse cat", "cat", 3))     # Output: 22


"""
# [💪 Challenge ✨5.5] Censor Words in a List =========================================================================
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
# def censor_words(sentence: str, banned: List[str]) -> str:
#     result = sentence
#     for i in range(len(banned)):
#         result = result.replace(banned[i], "***")
#     return result
    # -----------------------------------------------------------------------------------------------------------
    # | 👉 censor_words(sentence: str, banned: List[str]) 👈                                                   |
    # | Issue:                                                                                                  |
    # |     This will censor words inside other words. For example, banning "cat" in "educate" → "edu***e".     |
    # | Fix:                                                                                                    |
    # |     Using word boundaries and re.                                                                       |
    # -----------------------------------------------------------------------------------------------------------
def censor_words(sentence: str, banned: List[str]) -> str:
    for word in banned:
        pattern = r'\b' + re.escape(word) + r'\b'
        sentence = re.sub(pattern, '***', sentence, flags=re.IGNORECASE)
    return sentence

print("\n[💪 Challenge ✨5.5] Censor Words in a List -------------------------------------")
print("\t", censor_words("This is a bad sentence with dumb words", ["bad", "dumb"]))    # Output: "This is a *** sentence with *** words"


"""
# [💪 Challenge ✨5.6] Capitalize All First Letters ===================================================================
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
    wordList = text.split()
    result = ""
    for i in range(len(wordList)):
        if i > 0:
            result += " "
        result += wordList[i].capitalize()
    return result
    # -------------------------------------------------------------------------------------------------------------------------------------------
    # | 👉 smart_title(text: str) 👈                                                                                                           |
    # | Correct! This capitalizes each word manually, similar to .title(), but without the unwanted behavior like capitalizing "i'm" to "I'M".  |
    # -------------------------------------------------------------------------------------------------------------------------------------------

print("\n[💪 Challenge ✨5.6] Capitalize All First Letters -------------------------------")
print("\t", smart_title("tHis is a tItle"))                         # Output: "This Is A Title"


"""
# [💪 Challenge ✨6.1] Longest Repeated Substring =====================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Problem:
        Given a string s, find the longest substring that appears at least twice in s. Return that substring.
        If no repeated substring exists, return an empty string "".
    Function Signature:
        def longest_repeated_substring(s: str) -> str:
            pass
    Example:
        Input: "banana"                                             # Output: "ana"     🡸 "ana" appears twice
        Input: "abcab"                                              # Output: "ab"      🡸 "ab" appears twice
        Input: "abcdefg"                                            # Output: ""        🡸 no repeated substring
    Hints to get started:
        1. Use two loops to generate all substrings of s.
        2. Store substrings in a dictionary (or set) and check if they appear more than once.
        3. Keep track of the longest one you find.
# ----------------------------------------------------------------------------------------------------------------------
"""
# def longest_repeated_substring(s: str) -> str:
#     def _count_substring_occurrences(s: str) -> dict[str, int]:
#         seen = {}
#         for i in range(len(s)):
#             for j in range(i + 2, len(s) + 1):
#                 substring = s[i:j]
#                 seen[substring] = seen.get(substring, 0) + 1
#         return seen
#    
#     def _get_max_occurrence(substring_counts: dict[str, int]) -> int | None:
#         if not substring_counts:
#             return None
#         return max(substring_counts.values())
#    
#     def _get_keys_from_value(dictionary, value):
#         return [key for key, val in dictionary.items() if val == value and len(key) > 1]
#    
#     substring_dict = _count_substring_occurrences(s)
#     # print(f"Substring counts: {substring_dict}")
#
#     max_occurrence = _get_max_occurrence(substring_dict)
#     # print(f"Max occurrence: {max_occurrence}")
#
#     if max_occurrence == 1:
#         return ""
#     else:
#         longest_repeated_substrings = _get_keys_from_value(substring_dict, max_occurrence)
#         # print(f"Longest: {longest_repeated_substrings}")
#
#         if len(longest_repeated_substrings) == 1:
#             return [longest_repeated_substrings[0]]
#         else:
#             max_length = 0
#             for item in longest_repeated_substrings:
#                 if max_length < len(item):
#                     max_length = len(item)
#            
#             result = []
#             for item in longest_repeated_substrings:
#                 if len(item) == max_length:
#                     result.append(item)
#             return result
    # -----------------------------------------------------------------------------------------------------------------------
    # | 👉 longest_repeated_substring(s: str) 👈                                                                           |
    # | What you're doing right:                                                                                            |
    # |     - You're generating all substrings of length ≥ 2 — good!                                                        |
    # |     - You're counting occurrences with a dictionary — efficient for this level.                                     |
    # |     - You're extracting substrings with the max count — solid logic.                                                |
    # |     - You're checking substring length to ensure you return the longest.                                            |
    # | 🚨 Issue (A few things to fix): 🚨                                                                                 |
    # |     1. Function return type mismatch:                                                                               |
    # |         - Your function returns a list of strings, but the problem asks for only one longest repeated substring.    |
    # |         - If there are ties, any one longest repeated substring is okay.                                            |
    # |     2. Unnecessary filtering logic:                                                                                 |
    # |         - You're finding all substrings with the highest occurrence and then checking which is longest —            |
    # |           but for this challenge, you only need the longest repeated one.                                           |
    # -----------------------------------------------------------------------------------------------------------------------
def longest_repeated_substring(s: str) -> str:
    seen = {}
    longest = ""
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            seen[substring] = seen.get(substring, 0) + 1
            if seen[substring] > 1 and len(substring) > len(longest):
                longest = substring
    return longest

print("\n[💪 Challenge ✨6.1] Longest Repeated Substring ----------------------------------")
print("\t", longest_repeated_substring("banana"))                   # Output: "ana"
print("\t", longest_repeated_substring("abcab"))                    # Output: "ab"
print("\t", longest_repeated_substring("abcdefg"))                  # Output: ""
print("\t", longest_repeated_substring("aabbaabbaabb"))             # Output: "aabbaabb"


"""
# [💪 Challenge ✨6.2] Suffix Array + Longest Repeated Substring ======================================================
# ----------------------------------------------------------------------------------------------------------------------
    (Advanced Challenge)
    Problem:
        Write a function that returns the longest repeated substring in a given string using a suffix array
        + longest common prefix (LCP) method, which is far more efficient than brute force for larger strings.
    Goal:
        Find the longest substring that appears at least twice in the string.
    Function Signature:
        def longest_repeated_substring_adv(s: str) -> str:
            pass
    Example:
        longest_repeated_substring("banana")                        # Output: "ana"
    Guideline:
        1. Generate all suffixes of the string.
        2. Sort them.
        3. Compare adjacent suffixes to find the longest common prefix (LCP).
        4. Track the longest repeated substring.
# ----------------------------------------------------------------------------------------------------------------------
    ✏️ Step-by-Step Guide ✏️
    Step 1: Build All Suffixes
        - A suffix is a substring that starts at some index i and goes to the end.
          For example, for "banana" → ['banana', 'anana', 'nana', 'ana', 'na', 'a']
    Step 2: Sort the Suffixes
        - Sorting puts similar substrings next to each other.
        - After sorting "banana"’s suffixes:
                → ['a', 'ana', 'anana', 'banana', 'na', 'nana']
    Step 3: Compare Adjacent Suffixes
        - Find the longest common prefix (LCP) between every pair of adjacent suffixes.
        - Keep track of the longest LCP.
    Step 4: Return the Longest One 🡸 That’s your answer!
# ----------------------------------------------------------------------------------------------------------------------
"""

def longest_repeated_substring(s: str) -> str:
    if not s:
        return ""

    # Step 1: Create suffixes
    # -------------------
    # | Index   Suffix  |
    # | 0       banana  |
    # | 1       anana   |
    # | 2       nana    |
    # | 3       ana     |
    # | 4       na      |
    # | 5       a       |
    # -------------------
    suffixes = [s[i:] for i in range(len(s))]

    # Step 2: Sort suffixes lexicographically, similar substrings will appear next to each other.
    #         By comparing each pair of adjacent suffixes, we can find substrings that are repeated.
    # ❓ Why compare adjacent ones only? ❓
    #         Because sorting groups similar patterns together — any repeated substring will show up at the beginning of multiple suffixes that are next to each other in the sorted list.
    # -------------------
    # | Sorted Suffixes |
    # | 'a'             |
    # | 'ana'           |
    # | 'anana'         |
    # | 'banana'        |
    # | 'na'            |
    # | 'nana'          |
    # -------------------
    suffixes.sort()

    # Step 3: Compare adjacent suffixes for their common prefix
    #         We now compute the Longest Common Prefix (LCP) for each pair:
    # ---------------------------------------------------
    # | Pair					LCP                     |
    # | 'a' and 'ana'			'a'                     |
    # | 'ana' and 'anana'		'ana' ← longest so far  |
    # | 'anana' and 'banana'	''                      |
    # | 'banana' and 'na'		''                      |
    # | 'na' and 'nana'			'na'                    |
    # ---------------------------------------------------
    # 👇 This function finds the longest common prefix by comparing characters one by one until they differ.
    def lcp(s1, s2): # 🔧 LCP Function Example
        i = 0
        while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
            i += 1
        return s1[:i]

    # Step 4: Track and Return the Longest One
    #         - Among all LCPs we found: 'a', 'ana', '', '', 'na'
    #         - The longest one is 'ana', which appears more than once (in "banana" and "anana")
    #         So we return 'ana' as the answer.
    longest = ""
    for i in range(len(suffixes) - 1):
        common = lcp(suffixes[i], suffixes[i + 1])
        if len(common) > len(longest):
            longest = common

    return longest

print("\n[💪 Challenge ✨6.2] Suffix Array + Longest Repeated Substring -------------------")
print("\t", longest_repeated_substring("banana"))                   # Output: "ana"
print("\t", longest_repeated_substring("mississippi"))              # Output: "issi"


"""
# [💪 Challenge ✨7.1] Custom String Cleanup ========================================================================== *** I got different output from ChatGPT and still couldn't find solution.
# ----------------------------------------------------------------------------------------------------------------------
    (Practice Challenge)
    Problem:
        Write a function that clean up the given text by ...
        - Replaces multiple spaces with a single space              ⇐ Removing extra spaces
        - Removes punctuation (except periods and commas)           ⇐ Standardizing punctuation spacing
        - Ensures there's only one space after each period or comma ⇐ Removing unwanted characters if necessary (depending on scope)
    Function Signature:
        def cleanup_text(text: str) -> str
            pass
    Example:
        cleanup_text("Hello,,   world!! This   is... a test,,   okay?")         # Output: "Hello, world This is a test, okay"
# ----------------------------------------------------------------------------------------------------------------------
"""
def cleanup_text(text: str) -> str:
    if not text:
        return ""
    # 1. Normalize all types of whitespace (tabs, newlines, multiple spaces)
    text = text.replace("\t", " ").replace("\n", " ").replace("\r", " ")        # Replace tabs and newlines with spaces.
    text = re.sub(r'\s+', ' ', text)                                            # Normalize whitespace — collapse multiple spaces into a single space.
    # 2. Remove space(s) before punctuation
    text = re.sub(r'\s+([,.!?;:])', r'\1', text)                                # Replace all instances of whitespace before punctuation with the punctuation itself. 🡺 \s+ = one or more spaces 🡺 ([,.!?;:]) = followed by punctuation             ⇐ "hello , world ! " → "hello, world!"
    # 3. Ensure a space after punctuation (if followed by a word character)
    text = re.sub(r'([,.!?;:])([^\s])', r'\1 \2', text)                         # Add a space after punctuation if it's directly followed by a non-space character.   🡺 ([,.!?;:]) = punctuation 🡺 ([^\s]) = any non-space character right after it ⇐ "Hello,world!" → "Hello, world!"
    # 4. Remove leading and trailing whitespace
    return text.strip()                                                         # Remove leading and trailing whitespace — trim start/end spaces.

print("\n[💪 Challenge ✨7.1] Custom String Cleanup ---------------------------------------")
print("\t", cleanup_text("Hello,,   world!! This   is... a test,,   okay?"))    # Output: "Hello, , world! ! This is. .. a test, , okay?"
print("\t", cleanup_text("   Hello\t\tworld! \n This   is  messy.  "))          # Output: "Hello world! This is messy."
print("\t", cleanup_text("Hello , world!This is messy .Really ?Yes!"))          # Output: "Hello, world! This is messy. Really? Yes!"
print("\t", cleanup_text("Hello ,world!This is good.Really?Yes!"))              # Output: "Hello, world! This is good. Really? Yes!"
print("\t", cleanup_text(" Hello ,   world!This is   a test. "))                # Output: "Hello, world! This is a test."

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------
    # | 👆 Explanation of the above function "def cleanup_text(text: str) -> str" Regular Expression in more detail (step-by-step): 👆                             |
    # | Step 1: Normalize whitespace                                                                                                                                |
    # |     1. Remove leading and trailing whitespace                                                                                                               |
    # |        - Use a method that strips spaces, tabs, or line breaks at the start and end.                                                                        |
    # |        - Why? It avoids weird spacing when you print or process the text later.                                                                             |
    # |     2. Replace all tabs (\t), newlines (\n), and carriage return (\r) with a single space.                                                                  |
    # |        - You want everything on one clean line, with readable spacing.                                                                                      |
    # |     3. Collapsing multiple consecutive spaces between words into a single space.                                                                            |
    # |        - If the text has too many spaces, you collapse them to just one.                                                                                    |
    # |     📌 You can use a regular expression for this if you're comfortable. 📌                                                                                 |
    # |                                                                                                                                                             |
    # | Step 2: Fix spacing around punctuation (Standardize punctuation spacing)                                                                                    |
    # |     1. Remove any space(s) before punctuation marks (like . , ? ! : ;)                                                                                      |
    # |        Look for a space followed by punctuation (like " ,"), and replace it with just the punctuation: ","                                                  |
    # |            Example: "hello , world" → "hello, world"                                                                                                        |
    # |     2. Ensure one space after punctuation mark, unless it’s already followed by space or is at the end.                                                     |
    # |            Example: "world!This" → "world! This"                                                                                                            |
    # |     3. Avoid doubling punctuation or spacing (like "Hello!! " → "Hello!")                                                                                   |
    # |     📌 We can use a regular expression to insert space after punctuation marks if it's missing or manual character-by-character checks to manage this. 📌  |
    # |     Hints for code:                                                                                                                                         |
    # |        - Use re.sub(r'\s+([,.!?;:])', r'\1', text) to remove space before punctuation                                                                       |
    # |        - Then, use re.sub(r'([,.!?;:])([^\s])', r'\1 \2', text) to insert space after punctuation if missing.                                               |
    # |                                                                                                                                                             |
    # | Step 3: Handle special symbols, remove or normalize special characters (Optional)                                                                           |
    # |     1. Decide which symbols (e.g., &, %, $) should be kept depending on your context.                                                                       |
    # |        For basic cleanup, remove symbols (like @, #, *, ^, etc.)                                                                                            |
    # |     2. Remove or replace non-printable or irrelevant symbols or emojis, unless they are part of the valid content, to clean text (If needed).               |
    # |        Keep only alphanumerics, basic punctuation, and whitespace.                                                                                          |
    # |        - You might also allow accented letters depending on the context.                                                                                    |
    # |     📌 This part depends on the use case. For example, "$100" may be meaningful in some contexts. 📌                                                       |
    # |                                                                                                                                                             |
    # | Step 4: Case formatting (Optional)                                                                                                                          |
    # |     - Depending on your use case, you may want to convert the text to                                                                                       |
    # |        - all lowercase or capitalize appropriately                                                                                                          |
    # |        - sentence case (The first letter of the sentence)                                                                                                   |
    # |        - title case (Capitalize Each Word)                                                                                                                  |
    # |     - This isn’t required for cleaning, but can improve readability.                                                                                        |
    # |                                                                                                                                                             |
    # | Step 5: Return the cleaned result                                                                                                                           |
    # |     After all transformations, return the final, cleaned-up version of the input text.                                                                      |
    # |                                                                                                                                                             |
    # | (Step 3 & Step 4 = optional, not include in the function "def cleanup_text(text: str) -> str" above.)                                                       |
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
# [💪 Challenge ✨7.2] Enhanced cleanup_text function =================================================================
# ----------------------------------------------------------------------------------------------------------------------
    Goal:
        Here's an enhanced version of the cleanup_text function that also:
        - Reduces repeated punctuation like "!!" or "??" to just "!" or "?"
        - Cleans up quotes and parentheses spacing
        - Keeps all prior cleanup steps
    Function Signature:
        def cleanup_text_enhance(text: str) -> str:
            pass
    Example:
        cleanup_text_enhance('Wow!!  "Really?" she asked.  (Unbelievable! )  ')         # Output: 'Wow! "Really?" she asked. (Unbelievable!)'
# ----------------------------------------------------------------------------------------------------------------------
"""
def cleanup_text_enhance(text: str) -> str:
    # Step 1: Avoid touching apostrophes inside words (like don't, he's)
    # So we'll temporarily protect them
    text = re.sub(r"(\w)'(\w)", r"\1{{APOSTROPHE}}\2", text)
    # Step 2: Add space after punctuation if not followed by space or quote
    text = re.sub(r'([.!?,])(?=[^\s"\'])', r'\1 ', text)
    # Step 3: Remove space before closing quotes (e.g. ? ")
    text = re.sub(r'([.!?,])\s+([\'"])', r'\1\2', text)
    # Step 4: Add space before an opening quote if not already spaced
    text = re.sub(r'(?<![\s])(["\'])(?=\w)', r' \1', text)
    # Step 5: Clean up extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Step 6: Restore apostrophes
    text = text.replace('{{APOSTROPHE}}', "'")
    return text

print("\n[💪 Challenge ✨7.2] Enhanced cleanup_text function ------------------------------")
print("\t", cleanup_text_enhance('Wow!!  "Really?" she asked.  (Unbelievable! )  '))    # Output: 'Wow! ! "Really?" she asked. (Unbelievable! )'
print("\t", cleanup_text_enhance('Wow!"Really?" she asked.'))                           # Output: 'Wow! "Really?" she asked.'
print("\t", cleanup_text_enhance("No, no! Don't do that. 'Stop!' he yelled."))          # Output: "No, no! Don't do that. 'Stop!' he yelled."
print("\t", cleanup_text_enhance('"Wait!"she said. "Now."'))                            # Output: '"Wait! "she said. "Now."'
print("\t", re.sub(r'([.!?,])(["\'])', r'\1 \2', 'Wow!"Really?" she asked.'))           # Output: 'Wow! "Really? " she asked.'
print("\t", re.sub(r'([.!?,])(?=["])', r'\1 ',   'Wow!"Really?" she asked.'))           # Output: 'Wow! "Really? " she asked.'

def cleanup_text_myEnhance(text: str) -> str:
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # | Regex: Effectively collapse the duplicates of special characters (a special character followed by one or more repetitions of the same special character)                                    |
    # |     replaced with just the single captured special character, while leaving the duplicate English alphabets untouched.                                                                      |
    # |                                                                                                                                                                                             |
    # | 👇 Explanation of the Regular Expression: 👇                                                                                                                                               |
    # | ([^a-zA-Z]):                                                                                                                                                                                |
    # |     matches any single character that is not an English alphabet. This effectively targets special characters and whitespace characters.                                                    |
    # |     ➞ [^...]: This is a negated character set. It matches any character that is not inside the brackets.                                                                                   |
    # |     ➞ a-zA-Z: Matches any uppercase or lowercase English alphabet.                                                                                                                         |
    # |     ➞ The parentheses () around this part create a capturing group. This means that the specific special character that is matched will be remembered by the regular expression engine.    |
    # |     If you don't want to touch the whitespace characters, use ([^a-zA-Z\s]), so the whitespace characters will also not be matched.                                                         |
    # |     ➞ \s: Matches any whitespace character (space, tab, newline, etc.).                                                                                                                    |
    # |     ➞ Putting it all together, ([^a-zA-Z\s]) matches any single character that is not an English alphabet and not a whitespace character. This effectively targets special characters.     |
    # | \1+:                                                                                                                                                                                        |
    # |     matches one or more consecutive repetitions of the special character that was captured in the first group.                                                                              |
    # |     ➞ \1: This is a backreference. It refers to the content of the first capturing group (the special character matched by ([^a-zA-Z])).                                                   |
    # |     ➞ +: This quantifier means "one or more" occurrences of the preceding element.                                                                                                         |
    # | r'\1':                                                                                                                                                                                      |
    # |     ➞ This is the replacement string in re.sub().                                                                                                                                          |
    # |     ➞ \1: It refers back to the content of the first capturing group (the single special character that was matched).                                                                      |
    # |                                                                                                                                                                                             |
    # | How the Code Works:                                                                                                                                                                         |
    # |     The re.sub() function finds all occurrences in the text that match the pattern: "a special character followed by one or more repetitions of the same special character".                |
    # |     When a match is found, it is replaced with just the single captured special character (\1).                                                                                             |
    # |     This ensures that:                                                                                                                                                                      |
    # |     - If you have !!!!, the first ! is captured, and the subsequent !!! are matched by \1+. The entire sequence is replaced by a single !                                                   |
    # |     - If you have ...., the first . is captured, and the subsequent ... are matched by \1+. The entire sequence is replaced by a single .                                                   |
    # |     - Duplicate English alphabets (like aaaa) will not be matched because they fall within the a-zA-Z part of the negated character set.                                                    |
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    text = re.sub(r'([^a-zA-Z])\1+', r'\1', text) # Not complete yet
    # text = re.sub(r'(.)\1+', r'\1', text)     ⇐ This regex pattern will collapse all characters, including alphabets.
    # text = re.sub(r'\\\\+', r'\\', text)      ⇐ This regex pattern will collapse duplicates \
    # text = re.sub(r',,+', r',', text)         ⇐ This regex pattern will collapse duplicates ,

    # # Step 1: Avoid touching apostrophes (') inside words (like don't, he's)
    # # So we'll temporarily protect them
    # text = re.sub(r"(\w)'(\w)", r"\1{{APOSTROPHE}}\2", text)
    # # Step 2: Add space after punctuation if not followed by space or quote
    # text = re.sub(r'([.!?,])(?=[^\s"\'])', r'\1 ', text)
    # # Step 3: Remove space before closing quotes (e.g. ? ")
    # text = re.sub(r'([.!?,])\s+([\'"])', r'\1\2', text)
    # # Step 4: Add space before an opening quote if not already spaced
    # text = re.sub(r'(?<![\s])(["\'])(?=\w)', r' \1', text)
    # # Step 5: Clean up extra spaces
    # text = re.sub(r'\s+', ' ', text).strip()
    # # Step 6: Restore apostrophes
    # text = text.replace('{{APOSTROPHE}}', "'")
    return text

print("\n[💪 Challenge ✨7.3] My enhanced cleanup_text ------------------------------------")
print("\t", cleanup_text_myEnhance('Wow!!  "Really?" she asked.  (Unbelievable! )  '))  # Output: 
print("\t", cleanup_text_myEnhance('Wow!"Really?" she asked.'))                         # Output: 
print("\t", cleanup_text_myEnhance("No, no! Don't do that. 'Stop!' he yelled."))        # Output: 
print("\t", cleanup_text_myEnhance('"Wait!"she said. "Now."'))                          # Output: 

input1 = "Hello!!!!     George.... How are you????"
output1 = text = re.sub(r'([^a-zA-Z])\1+', r'\1', input1)
print(f"Input:   '{input1}'")
print(f"Output:  '{output1}'")

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
print("\n[💪 Challenge ✨] ---------------------------------------------------------------")
print("\t", )# Output: 