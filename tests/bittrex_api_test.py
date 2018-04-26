import unittest, sys
sys.path.append("..")
from app.exchanges_api_module.bittrex import bittrex

class TestBittrex(unittest.TestCase):

	def setUp(self):
		pass

	def test_get_markets(self):
		self.assertTrue(bittrex.get_markets().status_code)

if __name__ == '__main__':
    unittest.main()
