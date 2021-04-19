import json
from more_itertools import chunked

batch_size = 100000

with open('pushshift_data/comments/2019-12-15.json', 'r') as f:

    # Since file sizes are extremely large, we split into batches
    chunks = list(chunked(f, batch_size))

    for chunk in chunks:
        print(len(chunk))
        comments = []
        for json_obj in chunk:
            comments.append(json.loads(json_obj))
