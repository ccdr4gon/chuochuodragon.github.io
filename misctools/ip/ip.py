import requests
from bs4 import BeautifulSoup
url='https://ip.cn'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
tag1=soup.p.code.string
tag2=soup.p.next_sibling.code.string
print(tag1)
print(tag2)