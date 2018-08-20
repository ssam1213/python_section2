# -*- coding: utf8 -*-

import sys, urllib.request as req
from urllib.parse import urlparse

url = "http://www.encar.com"

mem = req.urlopen(url)

# print(type(mem))
# print(type({}))
# print(type([]))
# print(type(()))

# print("geturl", mem.geturl())
# print("status", mem.status)
# print("headers", mem.getheaders())
# print("info", mem.info())
# print("getcode", mem.getcode())
# print("read", mem.read(50).decode("utf-8"))

print(urlparse("http://www.encar.com"))

# import sys; 
# print(sys.version)


