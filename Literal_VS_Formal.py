# Which is Faster: Literal or Formal definitions?
# - Literals ([], (), {}) are directly interpreted as their respective types at the bytecode level.
# - Formal (list(), tuple(), dict()) involves function calls, which add overhead.
# ✅ Literals are significantly run faster than formal in Python, because they don’t require a function call.

# What’s the Difference Between Formal and Literal in Python?
# -----------------------------------------------------------------------------------------------------------------
# | Aspect		    | Literal Definition					| Formal Definition                                   |
# |-----------------|---------------------------------------|-----------------------------------------------------|
# | Syntax		    | [], (), {}							| list(), tuple(), dict()                             |
# | Performance	    | Faster ✅							   | Slower (function call overhead) ❌                  |
# | Readability	    | More concise ✅					   | More explicit but verbose ❌                        |
# | Use Cases		| Recommended for quick declarations	| Useful in cases like dynamically constructing types |
# -----------------------------------------------------------------------------------------------------------------

# When to use formal definitions?
# - When dynamically creating a collection from an iterable.
# - When using the dict() constructor for keyword arguments.
# Otherwise, literals are preferred for better performance and readability.

my_list = list(range(10))            # Formal is useful here
my_dict = dict(name="Alice", age=30) # Readable key-value creation

# Example 1: --------------------------------------------------------------
import timeit

# Timing literals
literal_time = timeit.timeit("[], (), {}", number=1000000)

# Timing formal definitions
formal_time = timeit.timeit("list(), tuple(), dict()", number=1000000)

print(f"Literal time: {literal_time}")
print(f"Formal time: {formal_time}")
