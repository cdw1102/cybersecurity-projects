import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_scores.csv")

# Basic statistics
average_score = df["Score"].mean()
highest_score = df["Score"].max()
lowest_score = df["Score"].min()
pass_rate = (df["Score"] >= 75).mean() * 100

print("Average Score:", average_score)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Pass Rate:", pass_rate, "%")

# Visualization
plt.figure()
plt.bar(df["Student"], df["Score"])
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
