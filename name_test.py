import unittest

from name import get_name

class NameTest(unittest.TestCase):

	def setUp(slef):
		print('this is setUp method')

	def test_get_name(self):
		name = get_name()
		self.assertEqual(name, 'hello world')

unittest.main()