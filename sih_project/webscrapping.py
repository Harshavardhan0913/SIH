from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth',500)
import time
import requests
import random

page = requests.get("https://dare2compete.com/hackathons?filters=open&types=oppstatus")
print(page)

soup = bs(page.content, features='html.parser')
print(soup)
#x = soup.find_all(cla
#print(x)