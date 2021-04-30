class Tools:
	@classmethod
	def is_prime(cls, n):
		if n <= 1:
			return False
		if n <= 3:
			return True
		for i in range(2, n):
			if n % i == 0:
				return False
		return True
