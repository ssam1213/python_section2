
from bs4 import BeautifulSoup
import urllib.parse as rep
import sys
import io
import os
import urllib.request
# req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# html = urllib.request.urlopen(req).read()

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# HTML 가져오기
base = "https://search.naver.com/search.naver?where=image&query="
quote = rep.quote_plus("사자")
url = base + quote
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)
savePath ="/Users/wonboklee/Desktop/Python/examples_inflearn_NaverImage/"
try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

soup = BeautifulSoup(res, 'html.parser')
imageList = soup.select("div.img_area > a.thumb._thumb > img")

for i, img_list in enumerate(imageList, 1) :
    # print(img_list['data-source'])
    fullFileName = os.path.join(savePath, savePath+str(i) + ".jpg")
    urllib.request.urlretrieve(img_list['data-source'], fullFileName)
    
print('다운로드완료')
