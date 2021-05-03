import pandas as pd
from newspaper import Article

submissions_lib_dem_con_rep_df = pd.read_csv('data/raw-reddit-responses/submissions_top300_year_liberal_democrats_conservative_republicans.tsv', sep='\t')

articles_df = pd.DataFrame(
    columns=["submission id", "article headline", "article body", "bias"]
)
comments_df = pd.DataFrame(
    columns=["comment id", "submission id", "comment body", "bias"]
)