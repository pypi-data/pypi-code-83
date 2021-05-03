from ..models.cryptocurrency import Cryptocurrency
from ..models.comment import Comment
from ..models.author import Author

from bs4 import BeautifulSoup

class PageScraper:
	def __init__(self, _domain=''):
		self.domain = _domain
		self.cryptocurrencies = []
		self.comments = []
		self.authors = []
		self._temp_authors = []
		self.soup = None

	def get_soup(self, _decoded_content):
		try:
			self.soup = BeautifulSoup(_decoded_content, 'html.parser')
			return (False, self.soup)
		except:
			return ('Soup Is Not Working', '')

	def build_author_model_list(self, _author = ('', '', '', '')):
		_author_id, _author_name, _profile_link, _profile_pic = _author

		if _author_name in self._temp_authors:
			pass
		else:
			self._temp_authors.append(_author_name)

			authorModel = Author()
			authorModel._id = _author[0]
			authorModel.name = _author[1]
			authorModel.profile_link = _author[2]
			authorModel.profile_pic = _author[3]

			self.authors.append(authorModel)

	def build_comment_model_list(self, _html_content):

		decoded_content = str(_html_content.decode("utf-8"))

		_error, soup = self.get_soup(decoded_content)

		if _error == False:
			comments = soup.find_all('div', class_='comment')
			
			_comment_index = 0

			for _comment in comments:

				_author_id = _comment['data-user-id']
				_author_name = _comment.find_all('span', class_='commentUsername')[0].text.strip()
				_profile_link = self.domain + _comment.find('a', class_='js-user-link')['href']
				_profile_pic = _comment.find('a', class_='js-user-link').find('img')['src']

				_crypto_name = soup.find('h1', class_='float_lang_base_1').text.strip()

				cry = Cryptocurrency()
				cry.name = _crypto_name

				if _author_name == '{username}':
					continue

				self.build_author_model_list((_author_id, _author_name, _profile_link, _profile_pic))

				_comment_content = _comment.find_all()[0].find('span', class_='js-text').text.strip()
				_date = _comment.find('span', class_='js-date')['comment-date']

				commentModel = Comment()
				commentModel._id = _comment['id']
				commentModel.comment = _comment_content
				commentModel.time = _date
				commentModel.author_name = _author_name
				commentModel.cryptocurrency_name = cry.name

				self.comments.append(commentModel)
				
				_comment_index = _comment_index + 1

			return (self.comments[0:10], self.authors) # First 10 Comments

		else:

			print('Error Occurred')
			return False


	def build_cryptocurrency_model_list(self, html_content):

		cryptocurrency_model_list = []

		decoded_content = str(html_content.decode("utf-8"))

		_error, soup = self.get_soup(decoded_content)

		if _error == False:

			_crypto_table = soup.find('table', class_='allCryptoTlb').find('tbody').find_all('tr')

			if _crypto_table:

				for i, item in enumerate(_crypto_table):
					_id = i

					try:
						name = item.find('td', class_='cryptoName').text.strip()
					except:
						name = '-'
					
					try:
						short_name = item.find('td', class_='symb').text.strip()
					except:
						short_name = '-'
						
					try:
						link = self.domain + item.find('td', class_='cryptoName').find('a')['href']
					except:
						link = '-'
						
					try:
						price_usd = '$' + item.find('td', class_='price').text.strip()
					except:
						price_usd = '-'
					
					try:
						market_cap = item.find('td', class_='js-market-cap').text.strip()
					except:
						market_cap = '-'
						
					cryptocurrencyModel = Cryptocurrency()
					cryptocurrencyModel._id = _id
					cryptocurrencyModel.name = name
					cryptocurrencyModel.short_name = short_name
					cryptocurrencyModel.link = link
					cryptocurrencyModel.price_usd = price_usd
					cryptocurrencyModel.market_cap = market_cap
				
					cryptocurrency_model_list.append(cryptocurrencyModel)

				return cryptocurrency_model_list

			else:

				return False
		else:

			print('Error Occured While Crypto HTML Content Scraping')
			return False

	def convert_to_list(self, _class_in_array = []):

		_temp_list = []
		for model_class in _class_in_array:
			_temp_list.append(model_class.convert_dict())

		return _temp_list

	def comment_convert_to_list(self, _comment_class_in_array = []):
		_comments = self.convert_to_list(_comment_class_in_array)

		return _comments

	def author_convert_to_list(self, _author_class_in_array = []):
		_authors = self.convert_to_list(_author_class_in_array)
		
		return _authors

	def cryptocurrency_convert_to_list(self, _cryptocurrency_class_in_array = []):
		_cryptocurrencies = self.convert_to_list(_cryptocurrency_class_in_array)
		
		return _cryptocurrencies