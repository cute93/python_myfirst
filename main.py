import requests
from bs4 import BeautifulSoup
import os

inp = input('이미지 : ')
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='+inp

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
imglist = soup.find_all('a', class_='thumb _thumb')
if len(imglist) > 0:
    os.mkdir(inp)
    os.chdir(inp)
n=1
for img in imglist:
    i = img.find('img')
    imgsource = i.attrs['data-source']
    imgdata = requests.get(imgsource)
    if imgdata.ok == True:
        with open(inp+str(n)+'.jpg', 'wb') as f:
            f.write(imgdata.content)
            n+=1

    
