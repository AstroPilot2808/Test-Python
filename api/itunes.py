import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# we are storing the request's response in a variable for later use
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])

# json.dumps function formats the json text nicely


for result in response.json()["results"]:
    print(result["trackName"])