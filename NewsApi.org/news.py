# Import the NewsApiClient from the newsapi library
from newsapi import NewsApiClient

# Import the requests library to make HTTP requests
import requests

# Import the API key from the env module
from env import api_key

# Define the URL for the News API request, including the country and API key
url = f"https://newsapi.org/v2/everything?q=AI&sortBy=popularity&language=en&from=2024-11-14&to=2024-11-14&apiKey={api_key}"

# Make a GET request to the News API
response = requests.get(url)
# Parse the JSON response from the API
data = response.json()
# Extract the titles of all articles from the response
titles = [article['title'] for article in data['articles']]
# Print the list of article titles

# Limit the list to the first 10 titles
limited_titles = titles[:10]

# Print the list of limited article titles
print(limited_titles)