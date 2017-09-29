from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

download_dir = 'download'
base_url = 'http://pythonscraping.com'

def get_absolute_url(base_url, source):
	if source.startswith('http://www.'):
		url = 'http://' + source[11:]
	elif source.startswith('http://'):
		url = source
	elif source.startswith('www.'):
		url = 'http://' + source[4:]
	else:
		url = base_url + '/' + source
	if base_url not in url:
		return None
	return url

def get_download_path(base_url, absoulute_url, download_dir):
	print('base_url---> ' + base_url)
	print('absoulute_url---> ' + absoulute_url)
	print('download_dir---> ' + download_dir)
	path = absoulute_url.replace('www.', '')
	path = path.replace(base_url, '')
	path = path.replace('?', '')
	path = download_dir + path
	directory = os.path.dirname(path)

	if not os.path.exists(directory):
		os.makedirs(directory)

	return path


html = urlopen('http://www.pythonscraping.com')
bs_obj = BeautifulSoup(html, 'html.parser')
# 使用lambda函数选择首页上所有带有src属性的标签
download_list = bs_obj.find_all(src= True)

for download in download_list:
	# 对URL进行清理和标准化，获取文件的绝对路径
	file_url = get_absolute_url(base_url, download['src'])
	if file_url is not None:
		print(file_url)
		urlretrieve(file_url, get_download_path(base_url, file_url, download_dir))