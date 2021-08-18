import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.merriam-webster.com/word-of-the-day/2021-08-10")
soup = BeautifulSoup(page.content, 'html.parser')
dt = soup.find_all('span', class_='w-a-title margin-lr-0 margin-tb-1875em')[0].get_text()
w = soup.find_all('h1')[0].get_text()
wattr = soup.find_all('word-attributes')
mainattr = wattr.findall('span', class_='main-attr')[0].get_text()
syllables = wattr.findall('span', class_='word-syllables')[0].get_text()
print(dt.strip())
print(w.strip())
print(mainattr.strip() + '   ' + syllables.strip())
