import requests
r = requests.get('http://localhost/excerpt.txt')
for i, line in enumerate(r.text.split('\n')):
  if line.strip():
    print("Line %i: " %(i), line.strip())
