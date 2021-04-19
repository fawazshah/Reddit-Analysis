import json
import requests

res = requests.get('https://api.pushshift.io/reddit/search/comment/?q=science')
print(json.dumps(res.json()))