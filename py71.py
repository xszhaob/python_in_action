from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator


# 编写代码清洗数据
def clean_input(input):
	input = re.sub('\n+', ' ', input).lower()
	input = re.sub('\[[0-9]*\]', '', input)
	input = re.sub(' +', ' ', input)
	input = bytes(input, 'UTF-8')
	input = input.decode('ascii', 'ignore')

	clean_input = []
	input = input.split(' ')

	for item in input:
		# string.punctuation来获取Python所有的标点符号，
		# 单词两端的任何标点符号都会被去掉
		item = item.strip(string.punctuation)
		if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
			clean_input.append(item)

	return clean_input


def ngrams(input, n):
	input = clean_input(input)
	output = {}
	for i in range(len(input) - n + 1):
		ngram_tmp = ' '.join(input[i:i+n])
		if is_common(input[i:i+n]):
			continue
		if ngram_tmp not in output:
			output[ngram_tmp] = 0
		output[ngram_tmp] += 1
	return output

def is_common(ngram):
	common_words = ["the", "be", "and", "of", "a", "in", "to", "have", "it",
	"i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
	"they", "is", "an", "at", "but","we", "his", "from", "that", "not",
	"by", "she", "or", "as", "what", "go", "their","can", "who", "get",
	"if", "would", "her", "all", "my", "make", "about", "know", "will",
	"as", "up", "one", "time", "has", "been", "there", "year", "so",
	"think", "when", "which", "them", "some", "me", "people", "take",
	"out", "into", "just", "see", "him", "your", "come", "could", "now",
	"than", "like", "other", "how", "then", "its", "our", "two", "more",
	"these", "want", "way", "look", "first", "also", "new", "because",
	"day", "more", "use", "no", "man", "find", "here", "thing", "give",
	"many", "well"]
	for word in ngram:
		if word in common_words:
			return True
	return False


content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
ngrams = ngrams(content, 2)
sorted_n_grams = sorted(ngrams.items() ,key = operator.itemgetter(1), reverse = True)
print(sorted_n_grams)