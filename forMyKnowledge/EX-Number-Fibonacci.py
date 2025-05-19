"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 Fibonacci Numbers
(In mathematics, the Fibonacci sequence is a sequence in which each element is the sum of the two elements that precede it.)
# ----------------------------------------------------------------------------------------------------------------------
"""

# Recursive version
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

print("Fibonacci (Recursive):", fib_recursive(8))

# Iterative version
def fib_iterative(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for i in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr

print("Fibonacci (Iterative):", fib_iterative(8))

"""
# ----------------------------------------------------------------------------------------------------------------------
>Example: Let's say n = 5, we want to compute the 5th Fibonacci number.
⚡Fibonacci sequence (index starting at 0): 0 → 1 → 1 → 2 → 3 → 5
----------------------------------------------
| i | prev. | curr. | new curr = prev + curr |
----------------------------------------------
| 2 |   0   |   1   |    0 + 1 = 1           |
| 3 |   1   |   1   |    1 + 1 = 2           |
| 4 |   1   |   2   |    1 + 2 = 3           |
| 5 |   2   |   3   |    2 + 3 = 5           |
----------------------------------------------
-> Final curr = 5
✅ The for loop is for i in range(2, n+1) because:
    - range(2, n+1) generates numbers from 2 up to and including n.
    - In Python, range(a, b) includes a but excludes b, so it goes up to b-1.
    - So if we want to include n, we must do n+1.
✨ Short Answer:
    - range(2, n+1) → because we want to process up to n, not just n-1.
    - In Python, range(2, n) would stop at n-1 → not enough!
# ----------------------------------------------------------------------------------------------------------------------
"""