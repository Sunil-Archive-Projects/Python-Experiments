import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

i=1

for i in range(813,2000):

    page = requests.get("http://xkcd.com/"+str(i)).content
    soup = BeautifulSoup(page)
    comicImageBlock = soup.find("div",{"id":"comic"})
    comicImageTag = comicImageBlock.find("img")
    comicURL = "http:"+comicImageTag['src']
    comicTitle = comicImageTag['title']
    for char in comicTitle:
        if char in "?/\*.":
            print("Replacing:")
            comicTitle=comicTitle.replace(char,"")
    
   # print(comicTitle)
    try:
        urlretrieve(comicURL, "C:/Temp/Scrapes/xkcd/"+str(i)+"_"+comicTitle+".png")
    except Exception as e:
		#print("ERROR!!!"+str(e)+":"+str(i))
            continue
