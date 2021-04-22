# Reddit Political Bias Analysis

Part of my Masters' thesis work at Imperial College London.

### Determining available attributes of an object

Especially useful for objects from the Reddit API where attributes aren't
well documented.

To print all object attribute names + values in json format:

`print(json.dumps(vars(obj), default=lambda o: str(o)))`

use `dir()` if obj has no `__dict__` attribute