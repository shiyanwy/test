import requests
import json
import re
from bs4 import BeautifulSoup
#from docx import Document

url = "https://wenku.baidu.com/view/96aa5f28fad6195f312ba695.html"
#header =  {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
header = {'User-agent': 'Googlebot'}
res = requests.get(url , headers = header)
r = res.text
plist = []
soup = BeautifulSoup(r, "html.parser")
plist.append(soup.title.string)
for div in soup.find_all('div', attrs={"class": "bd doc-reader"}):
    plist.extend(div.get_text().split('\n'))
plist = [c.replace(' ', '') for c in plist]
plist = [c.replace('\x0c', '') for c in plist]
print(plist)
