import requests
from bs4 import BeautifulSoup
url="https://www.hackerearth.com/challenges/hackathon/"
r=requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
soup=BeautifulSoup(htmlcontent,'html.parser')
title=soup.title
#print(type(title.string))
anchors=soup.find_all('meta')
#print(anchors)
headings=soup.find_all('span',class_="challenge-list-title challenge-card-wrapper")
for link in headings:
    print(link.get_text())
