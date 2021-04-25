import json
import praw
from newspaper import Article
import pandas as pd


articles_df = pd.DataFrame(
    columns=["submission id", "article headline", "article body", "bias"]
)
comments_df = pd.DataFrame(
    columns=["comment id", "submission id", "comment body", "bias"]
)

ground_truths_df = pd.read_csv("data/corpus-balanced-classes.tsv", sep="\t")

reddit = praw.Reddit("bias-bot", user_agent="bias-detection:v1.0 (by Fawaz Shah)")

subreddits = [
    (reddit.subreddit("liberal"), "left"),
    (reddit.subreddit("democrats"), "left"),
    (reddit.subreddit("conservative"), "right"),
    (reddit.subreddit("republicans"), "right"),
]

for subreddit, ground_truth_bias in subreddits:

    print(f"\nr/{subreddit.display_name.upper()}\n")

    for submission in subreddit.top("year", limit=1000):

        # Only select posts that are link posts and have score > 10
        if submission.selftext == "" and submission.score > 10:

            # Scraping article content
            article = Article(submission.url)
            try:
                article.download()
                article.parse()
            except Exception as err:
                print("continuing...")
                continue

            new_row = {
                "submission id": submission.id,
                "article headline": submission.title,
                "article body": article.text,
                "bias": ground_truth_bias,
            }
            articles_df = articles_df.append(new_row, ignore_index=True)

            # Resolves instances of MoreComments in comment tree
            submission.comments.replace_more()

            comment_list = submission.comments.list()
            for comment in comment_list:
                new_row = {
                    'comment id': comment.id,
                    'submission id': comment._submission,
                    'comment body': comment.body,
                    'bias': ground_truth_bias,
                }
                comments_df = comments_df.append(new_row, ignore_index=True)
