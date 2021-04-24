from urllib.parse import urlparse
import pandas as pd

corpus = pd.read_csv('data/corpus-balanced-classes.tsv', sep='\t')

def get_domain(url):
    return urlparse(url).netloc

corpus['domain'] = corpus['source_url'].apply(get_domain)

corpus.to_csv('data/corpus-balanced-classes-domain.tsv', sep='\t', index=False)