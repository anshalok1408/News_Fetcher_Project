import requests

# Ask user for input
query = input("What are you interested in today?\n")

# Your API key
api = "cc776d59bedf41bc8da53433c5387c8b"

# API URL
url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api}"

# Print URL (optional, for debugging)
print(url)

# Make the request
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Get the articles
articles = data.get("articles", [])

# Print articles
for index, article in enumerate(articles, start=1):
    print(f"{index}. {article.get('title')}")
    print(f"Link: {article.get('url')}")
    print("\n********************\n")

