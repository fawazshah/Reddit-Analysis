import pandas as pd

submissions_df = pd.read_csv('data/assembled-data/submissions_top300_year_liberal_democrats_conservative.tsv', sep='\t')
comments_df = pd.read_csv('data/assembled-data/comments_top300_year_liberal_democrats_conservative.tsv', sep='\t')

print(len(submissions_df))
print(len(comments_df))

submission_ids = list(submissions_df['submission id'])
for i, row in comments_df.iterrows():
    if row['submission id'] not in submission_ids:
        print("hellooo")