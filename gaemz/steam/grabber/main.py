from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
import os
import re
import requests
import urllib

steam_free_games_urls = []

url = 'https://api.joyreactor.cc/graphql'

query = os.path.join(os.path.dirname(__file__),  "request2jr.graphql")
query = open(query, encoding="utf-8", mode="r").read()

variables = os.path.join(os.path.dirname(__file__),  "request2jr.json")
variables = open(variables, encoding="utf-8", mode="r")
variables = json.load(variables)

payload = {
    'query': query,
    "variables": variables
}

headers = {
    'content-type': 'application/json'
}

r = requests.post(url, json=payload, headers=headers)
json_data = json.loads(r.text)

posts = json_data['data']['blog']['postPager']['posts']

for post in posts:
    soup = BeautifulSoup(post["text"], 'html.parser')
    links = soup.find_all("a", href=True)
    for link in links:
        link_query = urlparse(link["href"]).query
        link_query = re.sub('^url=', '', link_query)
        link_query = urllib.parse.unquote(
            link_query, encoding='utf-8', errors='replace')
        if urlparse(link_query).hostname == 'store.steampowered.com':
            steam_free_games_urls.append(link_query)

a = 1
