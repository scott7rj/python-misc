import requests
from bs4 import BeautifulSoup


with open('/home/mauro/Documents/python/python-misc/grammaire_progressive.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')
    print(soup.title)
    count = 1
    for s in soup.find_all('img', class_='absimg'):
        url = s.get('src')
        r = requests.get(url, allow_redirects=True)
        f = '{}.jpg'.format(str(count))
        open(f, 'wb').write(r.content)
        count += 1

#page = requests.get('https://www.academia.edu/43710029/corriges_grammaire_progressive_du_francais_avec_600_exercices_niveau_intermediairepdf')
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.title)
#for s in soup.find_all('div', class_='ie_fix'):
#    #print(s.get('src'))
#    print(s.get_text())
