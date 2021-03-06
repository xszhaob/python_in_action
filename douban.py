﻿from urllib import parse,request
from bs4 import BeautifulSoup
import re
import csv
import io
import sys
import os


index = {'icn' : 'index-book250-all'}
url = 'https://book.douban.com/top250'
file_path = 'F:\douban\douban_book.csv'

# 获取书名 评分 描述
def get_title(url, index):
	data = parse.urlencode(index)
	req = request.Request(url + '?' + data)
	html = request.urlopen(req).read().decode('utf-8')
	bs_obj = BeautifulSoup(html, 'html.parser')
	links = bs_obj.findAll('div', {'class' : 'pl2'})
	for link in links:
		# print(link)
		book_name = get_book_name(link)
		desc = get_desc(link)
		star = get_star(link)
		print(book_name + '  ' + star + '  ' + desc)
		store_in_csv(book_name, star, desc)


# 获取书名
def get_book_name(link):
	text = link.findAll('a', href = re.compile('.*subject.*'))[0].get_text()
	text = re.sub('\n+', '', text)
	text = re.sub(' +', '', text)
	return text

# 获取描述
def get_desc(link):
	return link.find_next_siblings('p', {'class' : 'pl'})[0].get_text()

# 获取评分
def get_star(link):
	star_div = link.find_next_siblings('div', {'class' : 'star clearfix'})[0]
	return star_div.findAll('span', {'class' : 'rating_nums'})[0].get_text()

# 保存在csv文件中
def store_in_csv(book_name, star, desc):
	with open(file_path, 'a', encoding = 'gb18030', newline='') as file_obj:
		writer = csv.writer(file_obj, dialect='excel')
		writer.writerow([book_name, star, desc])

# 设置表头
def init_title():
	with open(file_path, 'a', encoding = 'gb18030', newline='') as file_obj:
		writer = csv.writer(file_obj, dialect='excel')
		writer.writerow(['书名', '评分', '描述'])


# 执行
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
if os.path.exists(file_path):
	os.remove(file_path)

init_title()
for val in range(0,10):
	if val != 0:
		index = {'start' : val * 25}
	get_title(url, index)