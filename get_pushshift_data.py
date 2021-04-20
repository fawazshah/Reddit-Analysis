import json

from more_itertools import chunked

batch_size = 100000


def sort(dct):
    return {key:value for (key, value) in sorted(dct.items())}


with open("pushshift_data/submissions/2013-09.json", "r") as f:

    # Since file sizes are extremely large, we split into batches
    chunks = list(chunked(f, batch_size))

    for chunk in chunks:
        for submission_json in chunk:

            # Converting comment from JSON into dict
            submission = json.loads(submission_json)

            if submission["subreddit"].lower() == "liberal":
                print(json.dumps(sort(submission)))
