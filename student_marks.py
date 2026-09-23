import matplotlib.pyplot as plt
import seaborn as sns

# Data
x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]

students = ["Arun", "Rahul", "Anil", "Kiran", "Ravi"]
marks = [85, 72, 90, 68, 78]

data = [55, 60, 65, 70, 70, 75, 80, 85, 90, 95]

sns.set_theme(style="whitegrid")

# 1. Line Plot
plt.figure()
plt.plot(x, y, marker="o")
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 2. Bar Plot
plt.figure()
sns.barplot(x=students, y=marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Scatter Plot
plt.figure()
sns.scatterplot(x=x, y=y, s=100)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 4. Histogram
plt.figure()
sns.histplot(data, bins=5, kde=True)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 5. Box Plot
plt.figure()
sns.boxplot(y=data)
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()