import requests

class bittrex(object):

	def get_markets():
		r = requests.get('https://bittrex.com/api/v1.1/public/getmarkets')
		return r

	def get_currencies():
		r = requests.get('https://bittrex.com/api/v1.1/public/getcurrencies')
		return r

	def get_balances():
		r = requests.get('https://bittrex.com/api/v1.1/account/getbalances?apikey=API_KEY')
		return r

	def sell_limit(data = [], *args):
		r = requests.get(\
			'https://bittrex.com/api/v1.1/market/selllimit?apikey=API_KEY&market=BTC-LTC&quantity=1.2&rate=1.3')
		return r

	def get_market_summery(ico):
		r = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-'+ico)
		return r
