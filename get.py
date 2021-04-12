import praw
from pprint import pprint

reddit = praw.Reddit("bias-bot", user_agent="bias-detection:v1.0 (by Fawaz Shah)")

liberal = reddit.subreddit("liberal")

for submission in liberal.top(limit=100):
    print(submission.title)
    print(submission.url)

    # Resolves instances of MoreComments in comment tree
    submission.comments.replace_more()

    comment_tree = submission.comments.list()
    pprint(len(comment_tree))
