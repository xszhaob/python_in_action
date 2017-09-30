from urllib.request import urlopen
from random import randint

def word_list_sum(word_list):
	sum = 0
	for word, val in word_list.items():
		sum += val
	return sum

# 这个算法实在是太牛逼了
def retrieve_random_word(word_list):
	rand_index = randint(1, word_list_sum(word_list))
	for word, val in word_list.items():
		rand_index -= val
		if rand_index <= 0:
			return word

def build_word_dict(text):
	text = text.replace('\n', '')
	text = text.replace('\"', '')

	punctuation = [',', '.', ';', ':']
	for symbol in punctuation:
		text = text.replace(symbol, ' ' + symbol + ' ')

	words = text.split(' ')
	words = [word for word in words if word != '']

	word_dict = {}
	for i in range(1, len(words)):
		if words[i -1] not in word_dict:
			word_dict[words[i -1]] = {}
		if words[i] not in word_dict[words[i - 1]]:
			word_dict[words[i - 1]][words[i]] = 0
		word_dict[words[i - 1]][words[i]] = word_dict[words[i - 1]][words[i]] + 1

	return word_dict



content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
word_dict = build_word_dict(content)

length = 100
chain = ''
current_word = 'I'
for i in range(0, length):
	chain += current_word + ' '
	current_word = retrieve_random_word(word_dict[current_word])

print(chain)