import pandas as pd

# Load cleaned CSV file
df = pd.read_csv("data/cleaned_trends.csv")

# Total posts
print("Total posts:", len(df))

# Average score
print("Average score:", df["score"].mean())

# Average comments
print("Average comments:", df["num_comments"].mean())

# Top 5 posts by score
top_posts = df.sort_values(by="score", ascending=False).head(5)

print("\nTop 5 posts by score:")
print(top_posts[["title", "score"]])

# Category-wise post count
category_count = df["subreddit"].value_counts()

print("\nPosts per category:")
print(category_count)

# Category with highest average score
avg_score_category = df.groupby("subreddit")["score"].mean()

print("\nAverage score per category:")
print(avg_score_category)