import urllib.request
import json

apikey = "3b0eaaf4aa2e4054a8a6c3718cf4bee1"
query = "politics"
url = f"https://gnews.io/api/v4/search?q={query}&lang=en&country=us&token={apikey}"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

for article in data["articles"]:
    print("Title:", article["title"])
    print("Source:", article["source"]["name"])
    print("Source URL:", article["source"]["url"])
    print("Article URL:", article["url"])
    print()