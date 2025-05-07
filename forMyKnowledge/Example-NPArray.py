import numpy as np

numpy1 = np.array([17.2, 20.0, 8.25, 9.50])
numpy2 = np.array([13.0, 24.0, 8.25, 9.0])
result = np.logical_and(numpy1 > 10, numpy2 < 20)
print(result)                                                       # Output: [ True False False False]
    # -------------------------------------------------------------------------------------------
    # | 👆 Explanation step by step: 👆                                                        |
    # | 1. numpy1 > 10                                                                          |
    # |       → Performs element-wise comparison: [17.2 > 10, 20.0 > 10, 8.25 > 10, 9.50 > 10]  |
    # |       → Results in: [True, True, False, False]                                          |
    # | 2. numpy2 < 20                                                                          |
    # |       → Performs element-wise comparison: [13.0 < 20, 24.0 < 20, 8.25 < 20, 9.0 < 20]   |
    # |       → Results in: [True, False, True, True]                                           |
    # | 3. np.logical_and(...)                                                                  |
    # |       → Performs element-wise logical AND between the two Boolean arrays above:         |
    # |         [True and True, True and False, False and True, False and True]                 |
    # |       → Final result: [True, False, False, False]                                       |
    # -------------------------------------------------------------------------------------------