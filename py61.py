from urllib.request import urlopen

text_page = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(text_page.read(), 'utf-8'))