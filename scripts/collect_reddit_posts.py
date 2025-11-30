"""
Script to collect Reddit posts about movies.
Run from project root: python scripts/collect_reddit_posts.py
"""
import sys
from pathlib import Path

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import requests
import pandas as pd
import time
import datetime
from langdetect import detect, LangDetectException
from src.data_utils import save_dataframe

# Configuration
SUBREDDITS = ["movies", "boxoffice", "DC_cinematic", "superman"]
QUERIES = [
    "new Superman movie",
    "James Gunn Superman",
    "Superman 2025",
    "Jurassic World Rebirth",
    "Smurfs",
    "Fantastic Four First Steps",
    "Fantastic Four",
]
START_DATE = datetime.datetime(2025, 7, 1, tzinfo=datetime.timezone.utc)
END_DATE = datetime.datetime(2025, 8, 31, tzinfo=datetime.timezone.utc)
TARGET_COUNT = 600  # Increased target

# User-Agent is critical to avoid immediate 429s
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def get_timestamp(dt):
    return int(dt.timestamp())


def fetch_posts(subreddit, query, start_ts, end_ts):
    posts = []
    search_query = f"{query} after:{start_ts} before:{end_ts}"

    url = f"https://www.reddit.com/r/{subreddit}/search.json"
    params = {
        "q": search_query,
        "restrict_sr": "on",
        "include_over_18": "on",
        "sort": "relevance",
        "t": "all",
        "limit": 100,
        "raw_json": 1,
    }

    after = None

    # Fetch up to 3 pages
    for _ in range(3):
        if after:
            params["after"] = after

        try:
            print(f"Fetching {subreddit} query='{query}' (after={after})...")
            response = requests.get(url, headers=HEADERS, params=params)

            if response.status_code != 200:
                print(f"Error {response.status_code}: {response.text}")
                break

            data = response.json()
            children = data.get("data", {}).get("children", [])
            after = data.get("data", {}).get("after")

            if not children:
                break

            for child in children:
                post = child["data"]
                created_utc = post.get("created_utc")

                # Filter by date strictly
                if created_utc < start_ts or created_utc > end_ts:
                    continue

                posts.append(
                    {
                        "id": post.get("id"),
                        "title": post.get("title"),
                        "selftext": post.get("selftext"),
                        "subreddit": post.get("subreddit"),
                        "created_utc": created_utc,
                        "author": post.get("author"),
                        "permalink": f"https://www.reddit.com{post.get('permalink')}",
                        "url": post.get("url"),
                        "score": post.get("score"),
                    }
                )

            if not after:
                break

            time.sleep(1)

        except Exception as e:
            print(f"Exception fetching {subreddit} {query}: {e}")
            break

    return posts


def filter_english(posts):
    english_posts = []
    for post in posts:
        text = f"{post['title']} {post['selftext']}"
        try:
            if len(text.strip()) < 3:  # Too short to detect
                continue
            lang = detect(text)
            if lang == "en":
                english_posts.append(post)
        except LangDetectException:
            continue
    return english_posts


def main():
    all_posts = []
    start_ts = get_timestamp(START_DATE)
    end_ts = get_timestamp(END_DATE)

    print(f"Collecting posts from {START_DATE} to {END_DATE}")

    for subreddit in SUBREDDITS:
        for query in QUERIES:
            posts = fetch_posts(subreddit, query, start_ts, end_ts)
            print(f"Found {len(posts)} posts for {subreddit}/{query}")

            # Filter English
            en_posts = filter_english(posts)
            print(f"  {len(en_posts)} were English")

            all_posts.extend(en_posts)

            # Sleep to be nice
            time.sleep(2)

            if len(all_posts) >= TARGET_COUNT * 1.5:  # Collect a bit more to be safe
                break
        if len(all_posts) >= TARGET_COUNT * 1.5:
            break

    # Deduplicate by ID
    df = pd.DataFrame(all_posts)
    if not df.empty:
        df = df.drop_duplicates(subset=["id"])
        print(f"Total unique posts collected: {len(df)}")

        # Save to data/raw/
        output_path = save_dataframe(df, "reddit_posts.csv", subfolder="raw")
        print(f"Saved to {output_path}")
    else:
        print("No posts collected.")


if __name__ == "__main__":
    main()

