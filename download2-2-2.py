# -*- coding: utf8 -*-
import urllib

imageUrl = "http://post.phinf.naver.net/20150527_274/whtjdgus1666_1432689219314TApr5_JPEG/mug_obj_143268921826930359.jpg"
htmlUrl = "http://google.com"
savePath1 = "/Users/wonboklee/Desktop/Python/test1.jpg"
savePath2 = "/Users/wonboklee/Desktop/Python/index.html"

f = urllib.urlopen(imageUrl).read()
f2 = urllib.urlopen(htmlUrl).read()
saveFile1 = open(savePath1, 'wb') #write binary
saveFile1.write(f)
saveFile1.close()

# 이게 좋다 close자동실행
with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드완료")