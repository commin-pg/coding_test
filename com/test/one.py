"""
위키 기사

"""
import urllib.request
import json
from collections import Counter



topic = input()
counter = Counter()

url = 'https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page={}'.format(topic)
data = json.load(urllib.request.urlopen(url))
aa = data['parse']['text']['*']

print(aa.count(topic))
