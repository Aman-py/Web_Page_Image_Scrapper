# WEB Page Image Scraper
import requests
from bs4 import *
from PIL import Image
import matplotlib.pyplot as plt
import os
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
link = input("Input Your Link: ")
req = requests.get(link)
soup = BeautifulSoup(req.text,'lxml')
imgs=soup.find_all('img')
k = 1
for i in imgs:
    try:
        url =i['src']
        print('Image Link:',k)
        print(url)
        response = requests.get(url,stream=True)
        img = Image.open(response.raw)
        plt.imshow(img)
        plt.close()
        img.save(desktop+'/Image_Scraping/{}.jpg'.format(str(k)))
    except:
        KeyError
    k+=1
