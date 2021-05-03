from datetime import datetime

class Comment:
	def __init__(self, __id='', _comment='', _date='', _author='', _cryptocurrency_name=''):
		self._id = __id
		self.comment = _comment
		self.time = _date
		self.author_name = _author
		self.cryptocurrency_name = _cryptocurrency_name
	
	def comment_datetime_to_time(self):
		date_time_str = self.time

		try:
			date_time_obj = datetime.strptime(str(date_time_str), '%Y-%m-%d %H:%M:%S')
			return str(date_time_obj.hour) + ':' + str(date_time_obj.minute) + ':' + str(date_time_obj.second)
		except:
			return date_time_str

	def __str__(self):
		return str(self.convert_dict())

	def convert_dict(self):
		return self.__dict__