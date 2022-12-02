# pp 65
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'http://localhost/excerpt.txt')
for i, line in enumerate(3 r.data.decode('utf-8').split('\n')):
  if line.strip():
    print("Line %i: " %(i), line.strip())
