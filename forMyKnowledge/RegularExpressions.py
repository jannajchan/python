"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 Regular Expressions (called REs, or regexes, or regex patterns)
    https://docs.python.org/3/library/re.html
    https://docs.python.org/3/howto/regex.html#regex-howto
# ----------------------------------------------------------------------------------------------------------------------
r = Python’s raw string notation for regular expression patterns
.   Period
!   Exclamation mark
?   Question mark
,   Comma

------------
| Brackets | are typically deployed in symmetric pairs, and an individual bracket may be identified as a "Left bracket" or "Right bracket" or, alternatively, an "Opening bracket" or "Closing bracket", respectively, depending on the directionality of the context.
------------
    https://en.wikipedia.org/wiki/Bracket
()  (Round) Brackets / Parentheses
[]  Square brackets
{}  Braces / Curly braces / Curly brackets
<>  Angle brackets / Chevrons

------------------
| Metacharacters |
------------------
	. ^ $ * + ? { } [ ] \ | ( )     They are not active inside classes.

.       (Dot/Period.) In the default mode, this matches any character except a newline.
        If the DOTALL flag has been specified, this matches any character including a newline.
        (?s:.) matches any character regardless of flags.

^       (Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
        Match the characters not listed within the class by complementing the set. This is indicated by including a '^' as the first character of the class.
        If the caret appears elsewhere in a character class, it does not have special meaning.
        For example:
            [^5] will match any character except '5'.
            [5^] will match either a '5' or a '^'.

$       Matches the end of the string or just before the newline at the end of the string, and in MULTILINE mode also matches before a newline.
            For example: foo matches both ‘foo’ and ‘foobar’, while the regular expression foo$ matches only ‘foo’.
        More interestingly, searching for foo.$ in 'foo1\nfoo2\n' matches ‘foo2’ normally, but ‘foo1’ in MULTILINE mode; 
        searching for a single $ in 'foo\n' will find two (empty) matches: one just before the newline, and one at the end of the string.

*       Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible.
            For example: ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.

+       Causes the resulting RE to match 1 or more repetitions of the preceding RE.
            For example: ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.

?       Causes the resulting RE to match 0 or 1 repetitions of the preceding RE.
            For example: ab? will match either ‘a’ or ‘ab’.

*?, +?, ??
        The '*', '+', and '?' quantifiers are all greedy; they match as much text as possible. 
        Sometimes this behaviour isn’t desired; if the RE <.*> is matched against '<a> b <c>', it will match the entire string, and not just '<a>'.
        Adding ? after the quantifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched.
            For example: Using the RE <.*?> will match only '<a>'.

{m}     Specifies that exactly m copies of the previous RE should be matched; fewer matches cause the entire RE not to match.
            For example: a{6} will match exactly six 'a' characters, but not five.

{m,n}   Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible.
            For example:
                a{3,5} will match from 3 to 5 'a' characters. 
                Omitting m specifies a lower bound of zero, and omitting n specifies an infinite upper bound.
                a{4,}b will match 'aaaab' or a thousand 'a' characters followed by a 'b', but not 'aaab'.
        The comma may not be omitted or the modifier would be confused with the previously described form.

{m,n}?  Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible.
        This is the non-greedy version of the previous quantifier.
            For example:
                on the 6-character string 'aaaaaa', a{3,5} will match 5 'a' characters, 
                while a{3,5}? will only match 3 characters.

{m,n}+  Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible without establishing any backtracking points.
        This is the possessive version of the quantifier above.
            For example: 
                on the 6-character string 'aaaaaa', a{3,5}+aa attempt to match 5 'a' characters, then, requiring 2 more 'a's, will need more characters than available and thus fail, 
                while a{3,5}aa will match with a{3,5} capturing 5, then 4 'a's by backtracking and then the final 2 'a's are matched by the final aa in the pattern.
                x{m,n}+ is equivalent to (?>x{m,n})

\       As in Python string literals, the backslash can be followed by various characters to signal various special sequences.
        It’s also used to escape all the metacharacters so you can still match them in patterns.
        For example:
            If you need to match a [ or \, you can precede them with a backslash to remove their special meaning: \[ or \\.

        Some of the special sequences beginning with '\' represent predefined sets of characters that are often useful, 
        such as the set of digits, the set of letters, or the set of anything that isn’t whitespace.
        For example:
            \w matches any alphanumeric character. If the regex pattern is expressed in bytes, this is equivalent to the class [a-zA-Z0-9_].
            If the regex pattern is a string, \w will match all the characters marked as letters in the Unicode database provided by the unicodedata module.
        Either escapes special characters (permitting you to match characters like '*', '?', and so forth), or signals a special sequence; special sequences are discussed below.
        If you’re not using a raw string to express the pattern, remember that Python also uses the backslash as an escape sequence in string literals;
        if the escape sequence isn’t recognized by Python’s parser, the backslash and subsequent character are included in the resulting string.
        However, if Python would recognize the resulting sequence, the backslash should be repeated twice.
        This is complicated and hard to understand, so it’s highly recommended that you use raw strings for all but the simplest expressions.

[]      Used to indicate a set of characters that you wish to match. In a set:
        - Characters can be listed individually.
            For example: [amk] will match 'a', 'm', or 'k'.
        - Ranges of characters can be indicated by giving two characters and separating them by a '-'.
            For example:
                [abc] will match any of the characters a, b, or c; This is the same as [a-c].
                [a-z] will match any lowercase ASCII letter.
                [0-5][0-9] will match all the two-digits numbers from 00 to 59.
                [0-9A-Fa-f] will match any hexadecimal digit.
                If - is escaped (e.g. [a\-z]) or if it’s placed as the first or last character (e.g. [-a] or [a-]), it will match a literal '-'.
        - Special characters except backslash lose their special meaning inside sets.
            For example:
                [(+*)] will match any of the literal characters '(', '+', '*', or ')'.
        - Backslash either escapes characters which have special meaning in a set such as '-', ']', '^' and '\\' itself 
        or signals a special sequence which represents a single character such as \xa0 or \n 
        or a character class such as \w or \S (defined below).
        Note that \b represents a single “backspace” character, not a word boundary as outside a set, 
        and numeric escapes such as \1 are always octal escapes, not group references. 
        Special sequences which do not match a single character such as \A and \Z are not allowed.
        - Characters that are not within a range can be matched by complementing the set.
        If the first character of the set is '^', all the characters that are not in the set will be matched.
            For example:
                [^5] will match any character except '5'.
                [^^] will match any character except '^'. ⇐ ^ has no special meaning if it’s not the first character in the set.
        - To match a literal ']' inside a set, precede it with a backslash, or place it at the beginning of the set.
            For example:
                Both [()[\]{}] and []()[{}] will match a right bracket, as well as left bracket, braces, and parentheses.
        - Support of nested sets and set operations as in Unicode Technical Standard #18 might be added in the future. 
        This would change the syntax, so to facilitate this change a FutureWarning will be raised in ambiguous cases for the time being. 
        That includes sets starting with a literal '[' or containing literal character sequences '--', '&&', '~~', and '||'. 
        To avoid a warning escape them with a backslash.

|       A|B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B.
        An arbitrary number of REs can be separated by the '|' in this way. This can be used inside groups (see below) as well. 
        As the target string is scanned, REs separated by '|' are tried from left to right. When one pattern completely matches, that branch is accepted. 
        This means that once A matches, B will not be tested further, even if it would produce a longer overall match. In other words, the '|' operator is never greedy. 
        To match a literal '|', use \|, or enclose it inside a character class, as in [|].

(...)   Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group; 
        the contents of a group can be retrieved after a match has been performed, and can be matched later in the string with the \number special sequence, described below. 
        To match the literals '(' or ')', use \( or \), or enclose them inside a character class: [(], [)].

(?...)  This is an extension notation (a '?' following a '(' is not meaningful otherwise). 
        The first character after the '?' determines what the meaning and further syntax of the construct is. 
        Extensions usually do not create a new group; (?P<name>...) is the only exception to this rule. Following are the currently supported extensions.
"""



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