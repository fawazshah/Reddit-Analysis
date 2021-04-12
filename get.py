import praw

reddit = praw.Reddit("bias-bot", user_agent="bias-detection:v1.0 (by Fawaz Shah)")

liberal = reddit.subreddit("liberal")
print(liberal.description)
