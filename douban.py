import urllib.request


index = {'icn' : 'index-book250-all'}
url = 'https://book.douban.com/top250'


req = urllib.request.Request(url,headers = index)
html = urllib.request.urlopen(req).read().decode('UTF-8')
print(html)