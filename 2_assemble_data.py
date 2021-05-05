import pandas as pd
from newspaper import Article

subreddit_bias_map = {
    "liberal": "left",
    "democrats": "left",
    "conservative": "right",
    "republicans": "right",
}

submissions = pd.read_csv(
    "data/raw-reddit-responses/submissions_top300_year_liberal_democrats_conservative_republicans.tsv",
    sep="\t",
)
comments = pd.read_csv(
    "data/raw-reddit-responses/comments_top300_year_liberal_democrats_conservative_republicans.tsv",
    sep="\t",
)

num_submissions = len(submissions)
num_comments = len(comments)

submissions_df = pd.DataFrame(
    columns=["submission id", "subreddit", "article headline", "article body", "bias"]
)
comments_df = pd.DataFrame(
    columns=["comment id", "submission id", "subreddit", "comment body", "bias"]
)

for i, submission in submissions.iterrows():

    print(f"Submission {i+1} / {num_submissions}")

    # Scraping article content
    article = Article(submission["url"])
    try:
        article.download()
        article.parse()
    except Exception as err:
        print(f"Error with {submission['url']}")
        continue

    ground_truth_bias = subreddit_bias_map[submission["subreddit"].lower()]

    new_row = {
        "submission id": submission["id"],
        "subreddit": submission['subreddit'].lower(),
        "article headline": submission["title"],
        "article body": article.text,
        "bias": ground_truth_bias,
    }
    submissions_df = submissions_df.append(new_row, ignore_index=True)
    submissions_df.to_csv(
        "data/assembled-data/submissions_top300_year_liberal_democrats_conservative_republicans.tsv",
        sep="\t",
        index=False,
    )


for i, comment in comments.iterrows():

    print(f"Comment {i+1} / {num_comments}")

    ground_truth_bias = subreddit_bias_map[comment["subreddit"].lower()]

    new_row = {
        "comment id": comment["id"],
        "submission id": comment["_submission"],
        "subreddit": comment['subreddit'].lower(),
        "comment body": comment["body"],
        "bias": ground_truth_bias,
    }
    comments_df = comments_df.append(new_row, ignore_index=True)
    comments_df.to_csv(
        "data/assembled-data/comments_top300_year_liberal_democrats_conservative_republicans.tsv",
        sep="\t",
        index=False,
    )
