# -*- coding: utf8 -*-
from bs4 import BeautifulSoup

fp = open("cars.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

def car_func(selector) : 
  print('car_func', soup.select_one(selector).string)

car_lamda = lambda q : print("car lamda", soup.select_one(q).string)

car_func("#gr") 
car_func("li#gr")
car_func("ul > li#gr")
# 띄어쓰기는 자손 선택자 (자식의 자식의 자식... 조건만 맞으면 다 가져옴)
car_func("#cars #gr") 
#자식 선택자  >
car_func("#cars > #gr")  
car_func("li[id='gr']")  

car_lamda("#gr") 
car_lamda("li#gr")
car_lamda("ul > li#gr")
# 띄어쓰기는 자손 선택자 (자식의 자식의 자식... 조건만 맞으면 다 가져옴)
car_lamda("#cars #gr") 
#자식 선택자  >
car_lamda("#cars > #gr")  
car_lamda("li[id='gr']")  