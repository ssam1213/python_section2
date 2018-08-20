import urllib.request as req

topBanner = "https://ssl.pstatic.net/tveta/libs/1195/1195854/481648bba7f7dae09402_20180712183336953.jpg"

rightBanner = "https://ssl.pstatic.net/tveta/libs/1197/1197851/f6bacbb11fa4f2021f5d_20180627143242536.jpg"

saveTop = "/Users/wonboklee/Desktop/Python/topbanner.jpg"
saveRight = "/Users/wonboklee/Desktop/Python/rightbanner.jpg"

req.urlretrieve(topBanner, saveTop)
req.urlretrieve(rightBanner, saveRight)
