class Cryptocurrency:
	def __init__(self, __id='', _name='', _short_name='', _link='', _price_usd='', _market_cap=''):
		self._id = __id
		self.name = _name
		self.short_name = _short_name
		self.link = _link
		self.price_usd = _price_usd
		self.market_cap = _market_cap
		# currency convert
		self.try_usd = 8.29
		self.euro_usd = 0.83
			
	def price_usd_convert_to_currency(self, currency_type = 'try'):
		# try = Turkish lira, Euro
		if currency_type == 'try':
			try:
				return str(float(self.price_usd.replace('$', '').replace(',', '')) * self.try_usd) + 'TL'
			except:
				return self.price_usd
		elif currency_type == 'euro':
			try:
				return '€' + str(float(self.price_usd.replace('$', '').replace(',', '')) * self.euro_usd)
			except:
				return self.price_usd
		else:
			return self.price_usd

	def chat_link(self):
		return self.link + '/chat'

	def __str__(self):
		return str(self.convert_dict())

	def convert_dict(self):
		return self.__dict__