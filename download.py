import numpy as np
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#from translate import translator - it not works 
# Error whn I install textblob lib 
def get_title(lnk):
	x = urlopen(lnk)
	bs=BeautifulSoup(x,'lxml')
	links=bs.find("div",{"class" : "item-list"})
	res=links.findAll("a",href=re.compile("(/european-union/)+([A-Za-z0-9_:()])+"))
	for line in res:
		print(line['title'])

get_title('https://europa.eu/european-union/about-eu/countries_en')
