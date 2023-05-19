import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("No Band Name Provided")

results = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

data = results.json()

for result in data["results"]:
    print(result["trackName"])