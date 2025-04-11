# The error "Expected expression" occurs because the %timeit (which is an IPython magic function) is specific to Jupyter Notebook 
# and is not valid Python syntax in a standard .py file. 
# Visual Studio Code, when running Python scripts, does not recognize Jupyter-specific magic commands 
# unless you're working in a Jupyter Notebook environment.

# The difference between %timeit and %%timeit in Python is based on where they are used and what they measure:
# ----------------------------------------------------------------------------------------------------------------------
# | Command  | Scope	  | Usage	                                             | Example                             |
# |----------|------------|------------------------------------------------------|-------------------------------------|
# | %timeit  | Line magic | Measures the execution time of a single line of code | %timeit [x**2 for x in range(1000)] |
# | %%timeit | Cell magic | Measures execution time for the entire cell          | %%timeit (on the first line)        |
# |          |            | (multiple lines of code)                             | followed by multiple lines of code  |
# ----------------------------------------------------------------------------------------------------------------------

# When to Use Each?
# - Use %timeit when measuring a single-line statement.
# - Use %%timeit when measuring multiple lines inside a Jupyter Notebook cell.

# 1. %timeit (Single Line Timing)
#    - Used to time a single statement in an interactive Python session (Jupyter Notebook or IPython).

# Example 1: --------------------------------------------------------------
## %timeit sum([x for x in range(1000)])

# Solution 1:
import timeit

# Measure the execution time of the sum operation
execution_time = timeit.timeit('sum([x for x in range(1000)])', number=1000)
print(f"Execution time 1: {execution_time} seconds")
# -------------------------------------------------------------------------

# 2. %%timeit (Multiple Lines Timing)
#    - Used when you want to time multiple lines of code in a Jupyter Notebook cell.
#    - The %%timeit must be the first line in the cell.

# Example 2: --------------------------------------------------------------
## %%timeit
## my_list = [x**2 for x in range(1000)]
## total = sum(my_list)

# Solution 2:
## import timeit <-- Already import in Example 1, so no need to import again

# Define the code to be timed as a function
def test_code():
    my_list = [x**2 for x in range(1000)]
    total = sum(my_list)

# Measure the execution time
execution_time = timeit.timeit(test_code, number=1000)
print(f"Execution time 2: {execution_time} seconds")
# -------------------------------------------------------------------------

# Example 3: --------------------------------------------------------------
## time = %timeit -o numpy.random.rand()
#           → Store the result in a variable for further analysis.
#           → Allows access to best, worst, and average times.
#           → Useful when comparing different functions or optimizing code.
##        %timeit np.random.rand()
#           → Just want to print the execution time without storing it.
# %timeit             → A built-in IPython magic function, runs the statement multiple times and reports the best execution time.
# -o                  → Stores the result of %timeit in a variable instead of just printing it.
# numpy.random.rand() → Generates a random number between 0 and 1 using NumPy.

# Solution 3:
## import timeit <-- Already import in Example 1, so no need to import again
import numpy as np

# Measure the execution time of numpy.random.rand()
execution_time = timeit.timeit('np.random.rand()', setup='import numpy as np', number=1000)
print(f"Execution time 3: {execution_time} seconds")
# -------------------------------------------------------------------------
