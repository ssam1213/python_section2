# -*- coding: utf8 -*-
from bs4 import BeautifulSoup

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("a")

a = soup.find_all("a", string="daum")
print(a)

for a in links : 
    # print('a', type(a), a)
    href = a.attrs['href']
    txt = a.string
    # print('txt', txt)
    # print('href', href)