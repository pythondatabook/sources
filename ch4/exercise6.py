# pp 67

import requests
import json
params = {
'q':'Python programming language',
'apiKey': 'your API key',
'pageSize': 5} 
r = requests.get('https://newsapi.org/v2/everything',params)
articles = json.loads(r.text)
for article in articles['articles']:
  print(article['title'])
  print(article['publishedAt'])
  print(article['url'])
  print()
