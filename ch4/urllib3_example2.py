# pp 66
import json
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://newsapi.org/v2/everything?q=Python programming language&apiKey=your_newsapi_key&pageSize=5')
articles = json.loads(r.data.decode('utf-8'))
for article in articles['articles']:
  print(article['title'])
  print(article['publishedAt'])  
  print(article['url'])
  print() 
