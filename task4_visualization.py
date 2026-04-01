import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/cleaned_trends.csv")

# -------- Graph 1: Posts per category --------
category_counts = df["subreddit"].value_counts()

plt.figure()
category_counts.plot(kind="bar")

plt.title("Posts per Category")
plt.xlabel("Category")
plt.ylabel("Number of Posts")

plt.show()


# -------- Graph 2: Average score per category --------
avg_score = df.groupby("subreddit")["score"].mean()

plt.figure()
avg_score.plot(kind="bar")

plt.title("Average Score per Category")
plt.xlabel("Category")
plt.ylabel("Average Score")

plt.show()