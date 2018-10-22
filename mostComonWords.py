import requests
import sys
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
url=sys.argv[1]
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))

c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
print (c.most_common())
