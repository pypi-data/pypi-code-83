class BaseConnector:
	def __init__(self):
		self.action_results = []

	def add_action_result(self, action_result):
		self.action_results.append(action_result)
		return action_result

	def get_action_identifier(self):
		raise NotImplementedError()
