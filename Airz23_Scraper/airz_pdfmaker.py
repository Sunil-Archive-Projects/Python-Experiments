import os 
#for os.system
import requests
from bs4 import BeautifulSoup
import itertools
#for zip() function

links_path="C:\Temp\Scrape\\airz23\\airz23_scrape_links.txt"
titles_path="C:\Temp\Scrape\\airz23\\airz23_scrape_titles.txt"

with open(links_path,'r') as linkFile,open(titles_path,'r') as titleFile:
	for urlLink,pdfTitle in zip(linkFile,titleFile):
		try:
			pdfTitle=pdfTitle.strip('\n')
			pdfTitle=pdfTitle.replace(" ", "")
			pdfTitle=pdfTitle.replace("?", "")
			urlLink=urlLink.strip('\n')
			cmd='phantomjs phantom_pdfMaker.js '+urlLink+' '+pdfTitle
			print(cmd)
			os.system(cmd)#add the phantomjs script with parameters here to execute in cmd
		except Exception as e:
			print(e)