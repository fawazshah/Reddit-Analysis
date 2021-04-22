import datetime as dt
import json
import requests

from psaw import PushshiftAPI

pushshift_api = PushshiftAPI()

start_epoch=int(dt.datetime(2021, 1, 1).timestamp())

res = pushshift_api.search_submissions(after=start_epoch,
                            subreddit='politics',
                            limit=10)

res = list(res)
print(json.dumps(dir(res[0]), default=lambda o: str(o)))


#res = requests.get('https://api.pushshift.io/reddit/search/comment/?q=science')
#print(json.dumps(res.json()))