import requests
import json
import os
import time
from datetime import datetime

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
headers = {"User-Agent": "TrendPulse/1.0"}
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}
def get_category(title):
    title = title.lower()
    for category, keywords in categories.items():
        for word in keywords:
            if word in title:
                return category
    return "technology"  # fallback
# Fetch IDs
response = requests.get(TOP_STORIES_URL, headers=headers)
story_ids = response.json()[:500]
collected_posts = []
for story_id in story_ids:
    try:
        res = requests.get(ITEM_URL.format(story_id), headers=headers)
        story = res.json()
        if story is None or "title" not in story:
            continue
        category = get_category(story["title"])
        post = {
            "post_id": story.get("id"),
            "title": story.get("title"),
            "subreddit": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", "unknown"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        collected_posts.append(post)
        # Stop at 125
        if len(collected_posts) >= 125:
            break
    except:
        print("Error:", story_id)
time.sleep(2)
# Save file
if not os.path.exists("data"):
    os.makedirs("data")
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"
with open(filename, "w") as f:
    json.dump(collected_posts, f, indent=4)
print(f"Collected {len(collected_posts)} posts. Saved to {filename}")