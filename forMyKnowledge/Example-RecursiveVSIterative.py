"""
# ----------------------------------------------------------------------------------------------------------------------
# Difference between Recursive VS Iterative Approach: (Example: Factorial Calculation)
# ----------------------------------------------------------------------------------------------------------------------
🧠 Recursive: A function that calls itself to solve smaller subproblems.
✅ Advantages of Recursion:
    - Very simple and elegant code, especially for problems like:
        - Tree traversal
        - Divide and conquer (like Merge Sort, Quick Sort)
        - Backtracking (like solving mazes)
❌ Disadvantages of Recursion:
    - Memory heavy → every function call uses stack memory.
    - Risk of Stack Overflow if recursion is too deep (for very large inputs).
    - Slower sometimes compared to iteration because of the overhead of many function calls.

>>> factorial(5) → 5 × factorial(4) → 5 × 4 × factorial(3) → ... and so on.
# ----------------------------------------------------------------------------------------------------------------------
"""

# Recursive version
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

print("Factorial (Recursive):", factorial_recursive(5))

"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 Iterative: Solving a problem using loops (like for, while) without calling itself.
✅ Advantages of Iteration:
    - Faster because no overhead of function calls.
    - Memory efficient → no deep call stack.
    - Safe for large inputs.
❌ Disadvantages of Iteration:
    - Sometimes code is more complex and harder to visualize, especially for problems that naturally "branch" like trees or recursive math patterns.

>>> We loop and build the answer step-by-step.
# ----------------------------------------------------------------------------------------------------------------------
"""

def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print("Factorial (Iterative):", factorial_iterative(5))

"""
# ----------------------------------------------------------------------------------------------------------------------
🔥 Quick Comparison Table:
-----------------------------------------------------------------------------------------------------------------
| Aspect        | Recursive                                     | Iterative                                     |
-----------------------------------------------------------------------------------------------------------------
| Code style    | Short, elegant, closer to math                | Longer, step-by-step                          |
| Memory usage  | High (stack frames for each call)             | Low (single loop)                             |
| Speed         | Sometimes slower (because of function calls)  | Faster (no function call overhead)            |
| Risk          | Stack overflow risk                           | No stack overflow                             |
| Best for      | Tree problems, Divide & Conquer, Backtracking | Simple loops, large datasets                  |
-----------------------------------------------------------------------------------------------------------------

🏆 When should you use recursion vs iteration?
-----------------------------------------------------------------
| If the problem looks like...                      | Choose... |
-----------------------------------------------------------------
| Divide into smaller subproblems (trees, graphs)   | Recursion |
| Straightforward looping (list, array, math)       | Iteration |
-----------------------------------------------------------------

✨ Short Summary:
    Recursion is like trusting your future self to solve the next piece.
    Iteration is like manually walking through step-by-step.
# ----------------------------------------------------------------------------------------------------------------------
"""