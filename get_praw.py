import json
import praw
from newspaper import Article
from pprint import pprint


reddit = praw.Reddit("bias-bot", user_agent="bias-detection:v1.0 (by Fawaz Shah)")

liberal = reddit.subreddit("liberal")


num_articles = 0
num_comments = 0

for submission in liberal.hot(limit=1000):
    print(submission.title)
    print(submission.url)
    print(submission.score)

    # Scraping article content
    article = Article(submission.url)
    article.download()
    article.parse()
    print(article.text)

    # Resolves instances of MoreComments in comment tree
    submission.comments.replace_more()

    comment_list = submission.comments.list()
    print(len(comment_list))
    num_comments += len(comment_list)
    num_articles += 1

    print(f"Number of articles so far: {num_articles}")
    print(f"Number of comments so far: {num_comments}")
