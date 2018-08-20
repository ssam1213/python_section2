# -*- coding: utf8 -*-
import urllib

imageUrl = "http://post.phinf.naver.net/20150527_274/whtjdgus1666_1432689219314TApr5_JPEG/mug_obj_143268921826930359.jpg"
htmlUrl = "http://google.com"
savePath1 = "/Users/wonboklee/Desktop/Python/test1.jpg"
savePath2 = "/Users/wonboklee/Desktop/Python/index.html"

urllib.urlretrieve(imageUrl, savePath1)
urllib.urlretrieve(htmlUrl, savePath2)
print("다운로드완료")
