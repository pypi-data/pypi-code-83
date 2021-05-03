class Author:
	def __init__(self, __id='', _name='', _profile_link='', _profile_pic=''):
		self._id = __id
		self.name = _name
		self.profile_link = _profile_link
		self.profile_pic = _profile_pic

	def is_contributor(self):
		if self.profile_link.find('contributors') == -1:
			return False
		return True
	
	def add_author(self, _author_object = {}):
		self.__dict__ = _author_object
		return self.__dict__

	def __str__(self):
		return str(self.convert_dict())

	def convert_dict(self):
		return self.__dict__