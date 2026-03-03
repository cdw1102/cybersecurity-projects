import pandas as pd
import matplotlib.pyplot as plt

# Simulated student data
data = {
    "Student": ["John", "Lisa", "Mark", "Anna", "James", "Emily", "David", "Sarah"],
    "Score": [85, 92, 78, 88, 90, 73, 95, 80]
}

df = pd.DataFrame(data)

# Basic statistics
average_score = df["Score"].mean()
highest_score = df["Score"].max()
lowest_score = df["Score"].min()

print("Average Score:", average_score)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)

# Visualization
plt.bar(df["Student"], df["Score"])
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
