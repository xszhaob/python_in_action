import urllib.request
from bs4 import BeautifulSoup
import random
import datetime
import re
import time


page = set()
random.seed(datetime.datetime.now())


# 获取页面所有的内链列表
def get_internal_links(bs_obj, include_url):
	internal_links = []
	for link in bs_obj.findAll('a', href = re.compile('^(\/|.*' + include_url + ')')):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internal_links:
				internal_links.append(link.attrs['href'])
	return internal_links

# 获取页面所有的外链列表
def get_external_links(bs_obj, exclude_url):
	external_links = []
	for link in bs_obj.findAll('a', href = re.compile('^(http|www)((?!' + exclude_url + ').)*$')):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in external_links:
				external_links.append(link.attrs['href'])
	return external_links

def split_address(address):
	return address.replace('http://', '').replace('https://', '').split('/')

def get_random_external_link(starting_page):
	html = urllib.request.urlopen(starting_page).read()
	bs_obj = BeautifulSoup(html, 'html.parser')
	external_links = get_external_links(bs_obj, split_address(starting_page)[0])
	if len(external_links) == 0:
		internal_links = get_internal_links(bs_obj, starting_page)
		if len(internal_links) == 0:
			return
		return get_external_links(bs_obj, internal_links[random.randint(0, len(internal_links) - 1)])
	else:
		return external_links[random.randint(0, len(external_links) - 1)]

def follow_external_only(starting_site):
	external_link = get_random_external_link(starting_site)
	if external_link != None:
		print(external_link)
		time.sleep(random.randint(0, 10))
		follow_external_only(external_link)


#follow_external_only('https://baike.baidu.com/item/%E8%BE%A9%E6%8A%A4%E4%BA%BA/13023027?fr=aladdin')


all_ext_links = set()
all_int_links = set()

def get_all_external_links(site_url):
	html = urllib.request.urlopen(site_url).read()
	bs_obj = BeautifulSoup(html, 'html.parser')
	internal_links = get_internal_links(bs_obj, split_address(site_url)[0])
	external_links = get_external_links(bs_obj, split_address(site_url)[0])
	for link in external_links:
		all_ext_links.add(link)
		print(link)
	for link in internal_links:
		if link not in all_int_links:
			try:
				# print("即将获取连接的URL是：" + link)
				all_int_links.add(link)
				get_all_external_links(link)
			except Exception as e:
				continue
				# print("获取URL" + link + "的外链接失败，异常信息：")
				# print(e)


# get_all_external_links('https://baike.baidu.com/item/%E8%BE%A9%E6%8A%A4%E4%BA%BA/13023027?fr=aladdin')
# site_url = 'https://baike.baidu.com/item/%E8%BE%A9%E6%8A%A4%E4%BA%BA/13023027?fr=aladdin'
# html = urllib.request.urlopen(site_url).read()
# bs_obj = BeautifulSoup(html, 'html.parser')
# links = get_internal_links(bs_obj, site_url)
# print(links)
# internal_links = get_internal_links(bs_obj, split_address(site_url)[0])
# for link in internal_links:
# 	print(link)
# 	sp = split_address(site_url)
# 	print(sp)
# 	re_com = re.compile('^(/|.*' + sp[0] + ')')
# 	strs = re_com.findall(link)
# 	print(strs)