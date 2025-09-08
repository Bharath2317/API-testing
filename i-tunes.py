import requests
import sys
import json

term = sys.argv[1]
limit = int(input("Enter no of song you want to know: "))

url = f"https://itunes.apple.com/search?entity=song&limit={limit}&term={term}"

response = requests.get(url)

data = response.json()

for  result in data["results"]:
  trackname = result["trackName"]
  print(trackname)
