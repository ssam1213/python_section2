# -*- coding: utf8 -*-
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>Python beautifulsoup</h1>
        <p>태그선택자</p>
        <p>CSS선택자</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
# print(type(soup))

# print(soup.prettify())

h1 = soup.html.body.h1
print(h1)
# print(h1.string)
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
print(p2)
