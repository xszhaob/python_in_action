import unittest

from py3_douban import url, get_plain_text, hds
import numpy as np
from bs4 import BeautifulSoup

class Py3DoubanTest(unittest.TestCase):


	def random(self):
		print(np.random.random()*5)

	def test_get_plain_text(self):
		print(url)
		plain_text = get_plain_text(url, hds)

		print(plain_text)
		# soup = BeautifulSoup(bytes.decode('UTF-8'), 'html.parser')
		# print(soup)

unittest.main()