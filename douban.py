import urllib.request
from bs4 import BeautifulSoup
import sys
import re

print(sys.getfilesystemencoding())
index = {'icn' : 'index-book250-all'}
url = 'https://book.douban.com/top250'


req = urllib.request.Request(url,headers = index)
html = urllib.request.urlopen(req).read().decode('utf-8')
bs_obj = BeautifulSoup(html, 'html.parser')
links = bs_obj.findAll('div', {'class' : 'pl2'})
# for link in links:
# 	for lc in link.contents:
# 		print(lc.string)
with open('douban_book.txt','w', encoding = 'UTF-8') as file_obj:
	for link in links:
		for lc in link.contents:
			if lc.string is not None:
				file_obj.write(lc.string)
