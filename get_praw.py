import json
import praw
from newspaper import Article
from pprint import pprint


reddit = praw.Reddit("bias-bot", user_agent="bias-detection:v1.0 (by Fawaz Shah)")

liberal = reddit.subreddit("liberal")


num_articles = 0
num_comments = 0

for submission in liberal.hot(limit=1000):
    print(f"\nArticle headline: {submission.title}")
    print(f"Article score: {submission.score}")

    # Scraping article content
    article = Article(submission.url)
    try:
        article.download()
        article.parse()
    except Exception as err:
        print(err)
        print("continuing...")
        continue

    # Resolves instances of MoreComments in comment tree
    submission.comments.replace_more()

    comment_list = submission.comments.list()
    print(f"Number of comments: {len(comment_list)}")
    num_comments += len(comment_list)
    num_articles += 1

    print(f"\nNumber of articles so far: {num_articles}")
    print(f"Number of comments so far: {num_comments}")
