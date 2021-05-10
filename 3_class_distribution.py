import pandas as pd

submissions = pd.read_csv('data/assembled-data/submissions_top300_year_liberal_democrats_conservative.tsv', sep='\t')
comments = pd.read_csv('data/assembled-data/comments_top300_year_liberal_democrats_conservative.tsv', sep='\t')

print(f"No. articles: {len(submissions)}")

print("Article distribution: ")
print(submissions['subreddit'].value_counts())

print(f"No. comments: {len(comments)}")

print("Comment distribution: ")
print(comments['subreddit'].value_counts())
