from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import json


random.seed(datetime.datetime.now())

def get_links(article_url):
	html = urlopen('http://en.wikipadia.org' + article_url).read()
	bs_obj = BeautifulSoup(html, 'html.parser')
	return bs_obj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)(?!:).)*$'))

def get_history_ips(page_url):
	page_url = page_url.replace('/wiki/', '')
	history_url = 'http://en.wikipedia.org/w/index.php?title=' + pageUrl + '&action=history'
	print(history_url)
	html = urlopen(page_url).read()
	bs_obj = BeautifulSoup(html, 'html.parser')
	ip_addresses = bs_obj.find_all('a', {'class' : 'mw-anonuserlink'})
	address_list = set()
	for ip_address in ip_addresses:
		address_list.add(ip_address.get_text())
	return address_list

def get_country(ip_address):
	try:
		response = urlopen('http://freegeoip.net/json/' + ipAddress).read().decode('UTF-8')
	except Exception as e:
		print('get_country has error')
		print(e)
		return None
	else:
		response_json = json.loads(response)
		response_json.get('country_code')


links = get_links('/wiki/Python_(programming_language)')

while(len(links) > 0):
	for link in links:
		print('----------------')
		history_ips = get_history_ips(links.attrs['href'])
		for history_ip in history_ips:
			county = get_country(history_ip)
			if county is not None:
				print(history_ip + ' is from ' + county)
	new_link = links[random.randint(0, len(links) - 1)].attrs['href']
	links = get_links(new_link)