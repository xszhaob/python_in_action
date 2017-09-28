from bs4 import BeautifulSoup,NavigableString
import re


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

def not_lacie(href):
	return href and not re.compile('lacie').search(href)

def surrounded_by_strings(tag):
	return (isinstance(tag.next_element, NavigableString)
		and isinstance(tag.previous_element, NavigableString))

def has_six_characters(css_class):
	return css_class is not None and len(css_class) == 6

soup = BeautifulSoup(html_doc, 'html.parser')
# for tag in soup.find_all(attrs = {'class' : re.compile('sis')}, id = 'link3'):
# 	print(tag)
# for tag in soup.find_all('a', class_ = re.compile('sis')):
# 	print(tag)
# for tag in soup.find_all(class_ = has_six_characters):
# 	print(tag)
# for tag in soup.find_all('p', class_ = 'story'):
# 	print(tag)
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
print(css_soup.select("p.strikeout"))