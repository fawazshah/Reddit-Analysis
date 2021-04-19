import json

n = 1000
comments = []
with open('pushshift_data/comments/2019-12-15.json', 'r') as f:
    first_n_lines = [next(f) for i in range(n)]
    for json_obj in first_n_lines:
        comments.append(json.loads(json_obj))

print(json.dumps(comments[0]))
