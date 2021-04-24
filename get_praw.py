import json
import praw
from newspaper import Article
import pandas as pd


reddit = praw.Reddit("bias-bot", user_agent="bias-detection:v1.0 (by Fawaz Shah)")

articles_df = pd.DataFrame(columns=['submission id', 'article headline', 'article body', 'bias'])
comments_df = pd.DataFrame(columns=['comment id', 'submission id', 'comment body', 'bias'])
ground_truths_df = pd.read_csv('data/corpus-balanced-classes.tsv', sep='\t')

subreddits = [
    (reddit.subreddit("liberal"), 'left'),
    (reddit.subreddit("democrats"), 'left'),
    (reddit.subreddit("conservative"), 'right'),
    (reddit.subreddit("republicans"), 'right'),
]

num_articles = 0
num_comments = 0

for subreddit, bias in subreddits:
    for submission in subreddit.top("year", limit=1000):

        # Only select posts that are link posts and have score > 10
        if submission.selftext == "" and submission.score > 10:



            #print(f"\nArticle headline: {submission.title}")

            # Scraping article content
            article = Article(submission.url)
            try:
                article.download()
                article.parse()
                #print(article.text)
            except Exception as err:
                print(err)
                print("continuing...")
                continue

            # Resolves instances of MoreComments in comment tree
            submission.comments.replace_more()

            comment_list = submission.comments.list()

            num_comments += len(comment_list)
            num_articles += 1

            #print(f"\nNumber of articles so far: {num_articles}")
            #print(f"Number of comments so far: {num_comments}")
