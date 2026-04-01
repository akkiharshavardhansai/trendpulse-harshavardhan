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


# Show percentage distribution
dist = (df["subreddit"].value_counts(normalize=True) * 100).round(2)

print("\nCategory distribution (%):")
print(dist.rename("percentage"))

print("\nInsight:")

top_category = df["subreddit"].value_counts(normalize=True).idxmax()
top_percentage = (df["subreddit"].value_counts(normalize=True).max() * 100).round(2)

print(f"1. {top_category} dominates with {top_percentage}% of posts due to fallback keyword assignment.")
print("2. Other categories have low representation, affecting reliability.")
print("3. Some smaller categories show higher average scores, indicating impactful posts.")
