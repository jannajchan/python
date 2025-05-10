"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 Returning closures or Higher-order functions.
# ----------------------------------------------------------------------------------------------------------------------
To create a helper function that uses if-else logic to return different inner functions depending on conditions.
This technique is often referred to as returning closures or higher-order functions.
🔍 Key Concepts
    - You’re defining functions inside a function.
    - You can return different functions dynamically based on logic.
    - These returned functions can later be called just like any other.
# ----------------------------------------------------------------------------------------------------------------------
"""
def get_math_function(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply
    else:
        def default(x, y):
            return None
        return default

print("\n[🌟 Example 1:]--------------------------------------------------")

# Usage:
add_func = get_math_function("add")
print("\t", "add_func(3, 5) =", add_func(3, 5))   # Output: 8

mul_func = get_math_function("multiply")
print("\t", "mul_func(3, 5) =", mul_func(3, 5))   # Output: 15


"""
# ----------------------------------------------------------------------------------------------------------------------
🔧 Goal: Recursive String Compressor Using Returned Helper Function
We'll create a function get_compressor that returns a recursive compressor function, optionally using a mode ("basic" or "extended") to switch behavior.

🧠 Benefits of This Pattern:
    - Flexible Design: You can easily switch behaviors without changing the core logic.
    - Testable Functions: Each returned function is self-contained.
    - Encapsulation: Keeps logic clean and modular.
# ----------------------------------------------------------------------------------------------------------------------
"""
def get_compressor(mode="basic"):
    def basic_compress(s: str) -> str:
        def _compress(index, current_char, count):
            if index == len(s):
                return current_char + str(count)

            if s[index] == current_char:
                return _compress(index + 1, current_char, count + 1)
            else:
                return current_char + str(count) + _compress(index + 1, s[index], 1)

        if not s:
            return ""
        return _compress(1, s[0], 1)

    def extended_compress(s: str) -> str:
        def _compress(index, current_char, count):
            if index == len(s):
                return current_char + (str(count) if count > 1 else "")

            if s[index] == current_char:
                return _compress(index + 1, current_char, count + 1)
            else:
                part = current_char + (str(count) if count > 1 else "")
                return part + _compress(index + 1, s[index], 1)

        if not s:
            return ""
        return _compress(1, s[0], 1)

    # Return function depending on mode
    if mode == "basic":
        return basic_compress
    else:
        return extended_compress

print("\n[🌟 Example 2:]--------------------------------------------------")

# 🧪 How to Use It:
compress = get_compressor("basic")
print("\t", "compress(\"aaabbc\") =", compress("aaabbc"))             # Output: a3b2c1

compress_ext = get_compressor("extended")
print("\t", "compress_ext(\"aaabbc\") =", compress_ext("aaabbc"))     # Output: a3b2c


"""
# ----------------------------------------------------------------------------------------------------------------------
🧩 Final Goal:
We want a single function like get_string_processor(mode) that can return:
    - A compressor (basic or extended)
    - A decompressor (reverse of compression)
# ----------------------------------------------------------------------------------------------------------------------
"""
# ✅ Full Code: Compression + Decompression
def get_string_processor(mode="compress_basic"):
    def compress_basic(s: str) -> str:
        def _compress(index, current_char, count):
            if index == len(s):
                return current_char + str(count)
            if s[index] == current_char:
                return _compress(index + 1, current_char, count + 1)
            else:
                return current_char + str(count) + _compress(index + 1, s[index], 1)

        if not s:
            return ""
        return _compress(1, s[0], 1)

    def compress_extended(s: str) -> str:
        def _compress(index, current_char, count):
            if index == len(s):
                return current_char + (str(count) if count > 1 else "")
            if s[index] == current_char:
                return _compress(index + 1, current_char, count + 1)
            else:
                part = current_char + (str(count) if count > 1 else "")
                return part + _compress(index + 1, s[index], 1)

        if not s:
            return ""
        return _compress(1, s[0], 1)

    def decompress(s: str) -> str:
        i = 0
        result = ""
        while i < len(s):
            char = s[i]
            i += 1
            count = ""
            while i < len(s) and s[i].isdigit():
                count += s[i]
                i += 1
            result += char * (int(count) if count else 1)
        return result

    if mode == "compress_basic":
        return compress_basic
    elif mode == "compress_extended":
        return compress_extended
    elif mode == "decompress":
        return decompress
    else:
        raise ValueError("Unsupported mode. Choose: compress_basic, compress_extended, decompress")

print("\n[🌟 Example 3:]--------------------------------------------------")

# 🧪 Usage Examples:
# Get a basic compressor
compress_basic = get_string_processor("compress_basic")
print("\t", "compress_basic(\"aaabbc\") =", compress_basic("aaabbc")) # Output: a3b2c1

# Get an extended compressor
compress_ext = get_string_processor("compress_extended")
print("\t", "compress_ext(\"aaabbc\") =", compress_ext("aaabbc"))     # Output: a3b2c

# Get a decompressor
decompress = get_string_processor("decompress")
print("\t", "decompress(\"a3b2c\")", decompress("a3b2c"))             # Output: aaabbc
print("\t", "decompress(\"a3b2c1\")", decompress("a3b2c1"))           # Output: aaabbc
