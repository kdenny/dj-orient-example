from bs4 import BeautifulSoup

import requests

r = requests.get('https://www.washingtonpost.com/local/?nid=top_nav_local&utm_term=.085314ab7321')


### Append a user agent header to this request




data = r.text

print(data)

# soup = BeautifulSoup(data)
#
# for link in soup.find_all('a'):
#     print(link.get('href'))