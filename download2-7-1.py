# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import urllib.request as req

url = "http://finance.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')
# print('soup', soup.prettify())

top = soup.select('ul#topMyListNo1 > li')
# print(top)
for i,e in enumerate(top, 1) : 
  print(i, ", ", e.find("a").string, " : ", e.find('span').string)

