import pandas as pd

articles = pd.read_csv('data/articles_top300_year_liberal_democrats_conservative_republicans.tsv', sep='\t')
comments = pd.read_csv('data/comments_top300_year_liberal_democrats_conservative_republicans.tsv', sep='\t')

print(f"No. articles: {len(articles)}")
print(f"No. comments: {len(comments)}")

print(articles['subreddit'].value_counts())
