import json
import praw
from pprint import pprint

# To print all object attribute names + values in json format
# print(json.dumps(vars(obj), default=lambda o: str(o)))

reddit = praw.Reddit("bias-bot", user_agent="bias-detection:v1.0 (by Fawaz Shah)")

liberal = reddit.subreddit("liberal")

for submission in liberal.top(limit=100):
    print(submission.title)
    print(submission.url)

    # Resolves instances of MoreComments in comment tree
    submission.comments.replace_more()

    comment_list = submission.comments.list()
    comment = comment_list[0]