import requests

class LinkGrabber:
	def __init__(self, _page_url = ''):
		self.page_url = _page_url
		self.page_object = ''
		self.page_content = ''

	def get_page(self):
		if self.page_url:
			try:
				_headers = { 
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
				}

				self.page_object = requests.get(self.page_url, headers = _headers)
				return (False, self.page_object)
			except:
				return ('Get_Page_Exception_Error', '')
		else:
			return ('Page_Url_Not_Found', '')

	def get_page_content(self):
		_error, _page_object = self.get_page()

		if _error == False:
			self.page_content = _page_object.content
			return (False, self.page_content)
		else:
			return ('Page_Content_Error', '')

	def get_status_code(self):
		if self.page_object:
			return (False, self.page_object.status_code)
		else:
			return ('Page_Object_Not_Found', '')