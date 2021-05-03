import json
import praw
import pandas as pd
from pandas.io.json import json_normalize


submissions_df = pd.DataFrame()
comments_df = pd.DataFrame()

reddit = praw.Reddit("bias-bot", user_agent="bias-detection:v1.0 (by Fawaz Shah)")

subreddits = [
    reddit.subreddit("obama"),
    reddit.subreddit("hillaryclinton"),

    reddit.subreddit("liberal"),
    reddit.subreddit("democrats"),
    reddit.subreddit("conservative"),
    reddit.subreddit("republicans"),
]

for subreddit in subreddits:

    print(f"R/{subreddit.display_name.upper()}\n")

    for submission in subreddit.top("year", limit=300):

        # Only select posts that are link posts and have score > 10
        if submission.selftext == "" and submission.score > 10:

            submission_attributes = vars(submission)
            submissions_df = submissions_df.append(submission_attributes, ignore_index=True)
            print(submissions_df.shape)

            # Resolves instances of MoreComments in comment tree
            submission.comments.replace_more()

            comment_list = submission.comments.list()
            for comment in comment_list:

                # Only select comments with score > 10
                if comment.score > 10:
                    comment_attributes = vars(comment)
                    comments_df = comments_df.append(comment_attributes, ignore_index=True)
            print(comments_df.shape)
    
        # Save data to file after every submission
        submissions_df.to_csv('data/raw-reddit-responses/submissions.tsv', sep='\t', index=False)
        comments_df.to_csv('data/raw-reddit-responses/comments.tsv', sep='\t', index=False)
    