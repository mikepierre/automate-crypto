import requests

class bittrex(object):
	"""docstring for ClassName"""

	def get_markets():
		r = requests.get('https://bittrex.com/api/v1.1/public/getmarkets')
		return r