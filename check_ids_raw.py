import pandas as pd

submissions_df = pd.read_csv('data/raw-reddit-responses/submissions_top300_year_republican.tsv', sep='\t')
comments_df = pd.read_csv('data/raw-reddit-responses/comments_top300_year_republican.tsv', sep='\t')

print(len(submissions_df))
print(len(comments_df))

submission_ids = list(submissions_df['id'])
for i, row in comments_df.iterrows():
    if row['_submission'] not in submission_ids:
        print("Integrity error!")