# from newsapi import NewsApiClient
from urllib import response
import newsapi
import requests

# newsapi = NewsApiClient(api_key='29024c9e45b0423db6956e6a19ad233c')
API_KEY = '29024c9e45b0423db6956e6a19ad233c'
def get_articles_by_category(category):
    query_parameters={
        "category": category,
        "sortBy": "top",
        "country": "in",
        "apikey": API_KEY
    }

def _get_articles(params):
    responce = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []

    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})