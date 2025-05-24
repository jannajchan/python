import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

"""
# ----------------------------------------------------------------------------------------------------------------------
🧠 Graphs in Python
# ----------------------------------------------------------------------------------------------------------------------
"""

"""
# [💪 Challenge ✨1] Line Chart =======================================================================================
# ----------------------------------------------------------------------------------------------------------------------
"""
def lineChart():
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 5, 8, 3]

    plt.plot(x, y)
    plt.title('Line Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

print("\n[💪 Challenge ✨1] Line Chart ---------------------------------------------------")
lineChart()


"""
# [💪 Challenge ✨2] Bar Chart ========================================================================================
# ----------------------------------------------------------------------------------------------------------------------
"""
def barChart():
    categories = ['A', 'B', 'C', 'D']
    values = [25, 40, 30, 20]

    plt.bar(categories, values)
    plt.title('Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

print("\n[💪 Challenge ✨2] Bar Chart ----------------------------------------------------")
barChart()


"""
# [💪 Challenge ✨3] Pie Chart ========================================================================================
# ----------------------------------------------------------------------------------------------------------------------
"""
def pieChart():
    labels = ['Category A', 'Category B', 'Category C']
    sizes = [30, 45, 25]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Pie Chart')
    plt.show()

print("\n[💪 Challenge ✨3] Pie Chart ----------------------------------------------------")
pieChart()


"""
# [💪 Challenge ✨4] Histogram ========================================================================================
# ----------------------------------------------------------------------------------------------------------------------
"""
def histogram():
    data = np.random.randn(1000)

    plt.hist(data, bins=30, edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.show()

print("\n[💪 Challenge ✨4] Histogram ----------------------------------------------------")
histogram()


"""
# [💪 Challenge ✨5] Scatter Plot =====================================================================================
# ----------------------------------------------------------------------------------------------------------------------
"""
def scatterPlot():
    x = np.random.rand(50)
    y = 2 * x + 1 + 0.1 * np.random.randn(50)

    plt.scatter(x, y)
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

print("\n[💪 Challenge ✨5] Scatter Plot -------------------------------------------------")
scatterPlot()


"""
# [💪 Challenge ✨6] Box Plot =========================================================================================
# ----------------------------------------------------------------------------------------------------------------------
"""
def boxPlot():
    data = [np.random.normal(0, std, 100) for std in range(1, 4)]

    sns.boxplot(data=data)
    plt.title('Box Plot')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

print("\n[💪 Challenge ✨6] Box Plot -----------------------------------------------------")
boxPlot()


"""
# [💪 Challenge ✨7] Violin Plot ======================================================================================
# ----------------------------------------------------------------------------------------------------------------------
"""
def violinPlot():
    data = [np.random.normal(0, std, 100) for std in range(1, 4)]

    sns.violinplot(data=data)
    plt.title('Violin Plot')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

print("\n[💪 Challenge ✨7] Violin Plot --------------------------------------------------")
violinPlot()


"""
# [💪 Challenge ✨8] Heatmap ==========================================================================================
# ----------------------------------------------------------------------------------------------------------------------
"""
def heatmap():
    data = np.random.rand(10, 10)

    sns.heatmap(data, annot=True)
    plt.title('Heatmap')
    plt.show()

print("\n[💪 Challenge ✨8] Heatmap ------------------------------------------------------")
heatmap()


"""
# [💪 Challenge ✨9] Area Chart =======================================================================================
# ----------------------------------------------------------------------------------------------------------------------
"""
def areaChart():
    x = [1, 2, 3, 4, 5]
    y1 = [10, 15, 25, 30, 35]
    y2 = [5, 10, 20, 25, 30]

    plt.fill_between(x, y1, y2, color='skyblue', alpha=0.4)
    plt.title('Area Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

print("\n[💪 Challenge ✨9] Area Chart ---------------------------------------------------")
areaChart()


"""
# [💪 Challenge ✨10] Radar Chart =====================================================================================
# ----------------------------------------------------------------------------------------------------------------------
"""
def radarChart():
    labels = np.array(['A', 'B', 'C', 'D', 'E'])
    data = np.array([4, 5, 3, 4, 2])

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    data = np.concatenate((data, [data[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    plt.polar(angles, data, marker='o')
    plt.fill(angles, data, alpha=0.25)
    plt.title('Radar Chart')
    plt.show()

print("\n[💪 Challenge ✨10] Radar Chart -------------------------------------------------")
radarChart()