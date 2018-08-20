# -*- coding: utf8 -*-
from bs4 import BeautifulSoup

#CSS선택자 활용

html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")

h1 = soup.select_one("div#main > h1")
print(h1)

li = soup.select("div#main > ul.lecs > li")

for i in li : 
  print(type(i)) # <class 'bs4.element.Tag'>
  print(i.string)