from urllib import parse,request
from bs4 import BeautifulSoup
import sys
import re


index = {'icn' : 'index-book250-all'}
url = 'https://book.douban.com/top250'



def get_title(url, index):
	data = parse.urlencode(index)
	req = request.Request(url + '?' + data)
	print(req.get_full_url())
	html = request.urlopen(req).read().decode('utf-8')
	bs_obj = BeautifulSoup(html, 'html.parser')
	links = bs_obj.findAll('a', href = re.compile('.*subject.*'))

	with open('douban_book.txt','a', encoding = 'UTF-8') as file_obj:
		for link in links:
			if link.stripped_strings is not None and len(list(link.stripped_strings)) > 0:
				for string in link.stripped_strings:
					file_obj.write(string )
				print(link.parent.next_sibling)
				file_obj.write('\n')

for val in range(0,10):
	if val != 0:
		index = {'start' : val * 25}
	get_title(url, index)