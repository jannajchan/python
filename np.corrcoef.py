# np.corrcoef() is a function in NumPy that calculates the Pearson correlation coefficient between two datasets.
# (or within a matrix of datasets)

# What is Pearson Correlation Coefficient (r)?
# ค่าสถิติที่ใช้วัดความสัมพันธ์เชิงเส้น (Linear Relationship) ระหว่างตัวแปรสองตัว โดยค่าจะอยู่ในช่วง -1 ถึง 1

# Syntax: np.corrcoef(x, y=None, rowvar=True, bias=<no value>, ddof=<no value>)
# Parameters:
# -> x           – A 1D or 2D array-like object (list, NumPy array).
# -> y           – (Optional) If provided, calculates correlation between x and y.
# -> rowvar=True – If True, each row represents a variable and each column represents an observation.
#                  If False, each column represents a variable.

# Key Points:
# The Pearson correlation coefficient (r) ranges from -1 to 1 (การแปลความหมายของค่า r):
#  1            → ความสัมพันธ์เชิงบวกแบบสมบูรณ์ (Perfect Positive Correlation)
#  0.5 to  0.9  → ความสัมพันธ์เชิงบวกที่แข็งแรง
#  0            → ไม่มีความสัมพันธ์ (No Correlation)
# -0.5 to -0.9  → ความสัมพันธ์เชิงลบที่แข็งแรง
# -1            → ความสัมพันธ์เชิงลบแบบสมบูรณ์ (Perfect Negative Correlation)
# Used in statistics, machine learning, and data analysis to measure relationships between datasets.

# Example 1: Correlation between 2 Lists ----------------------------------------
# ✅ Interpretation: The correlation coefficient is 1, meaning x and y are perfectly correlated.
import numpy as np

def calculate_correlation(x, y):
    correlation_matrix = np.corrcoef(x, y)

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
correlation_matrix = np.corrcoef(a, b)
print("Pearson correlation coefficient:\n", correlation_matrix)

c = [10, 20, 30, 40, 50]
d = [15, 25, 35, 45, 55]
correlation_matrix = np.corrcoef(c, d)
pearson_r = correlation_matrix[0, 1]
print(f"Pearson correlation coefficient: {pearson_r:.2f}")

# Example 2: Correlation between multiple variables (2D Matrix) -----------------
# ✅ This shows that all variables are highly correlated.
data = np.array([[1, 2, 3], [2, 4, 6], [5, 10, 15]])
correlation_matrix = np.corrcoef(data)
print(correlation_matrix)
