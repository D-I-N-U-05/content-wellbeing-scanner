"""
Reddit Content Safety Scanner
Queries public metadata to test filtering parameters.
"""

import os

# Configuration for Reddit OAuth
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "")
USER_AGENT = "android:content-safety-filter:v1.0 (by /u/North_Opposite_6171)"

TARGET_SUBREDDITS = [
    "digitaldetox",
    "NoFap",
    "selfimprovement",
    "mentalhealth"
]

def check_post_flags(post_data):
    """Inspects post metadata boolean flags without storing text bodies."""
    return post_data.get("over_18", False)

if __name__ == "__main__":
    print("Safety scanner initialized.")
