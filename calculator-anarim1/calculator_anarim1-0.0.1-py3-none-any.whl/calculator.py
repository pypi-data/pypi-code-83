class Calculator:
	'''
	Simple calculator, consists of functions such as:
	Addition/Subtraction/Multiplication/Division/Root of number

	If one argument is passed (a), use calculator "memory" as second argument.
	"memory" is used as FIRST argument, except from Root function.

	All functions return floats with 2 decimal points!
	'''

	def __init__(self):    # Initialise calculator "memory"
		self.memory = 0

	def add(self, a, b=None):
		''' Print the sum of 'a' and 'b'(if provided), 
			otherwise 'a' and 'memory' '''	
		if b==None:
			c = self.memory+a
		else:
			c = a+b
		self.memory = c
		return (format(c, '.2f'))

	def sub(self, a, b=None):	# Subtraction function.	
		''' Subtracts 'b'(if provided) from 'a', 
			otherwise a from 'memory' '''
		if b==None:
			c = self.memory-a
		else:
			c = a-b
		self.memory = c
		return (format(c, '.2f'))

	def mul(self, a, b=None):	# Multiplication function.
		''' Multiplies 'a' by 'b'(if provided) 
			otherwise 'a' by 'memory' '''
		if b==None:
			c = self.memory*a
		else:
			c = a*b
		self.memory = c
		return (format(c, '.2f'))

	def div(self, a, b=None):	# Division function.
		''' Divides 'a' by 'b'(if provided), 
			otherwise 'memory' by 'a' '''
		try:					# Catch Zero Devision
			if b==None:
				c = self.memory/a
			else:
				c = a/b
			self.memory = c
			return (format(c, '.2f'))
		except ZeroDivisionError:
			return ("Division by 0")

	def nrt(self, a, b=None):	# Root of number function. First argument is used as Root power
		''' Returns nth(b)(if provided) root of 'a',
			otherwise nth(a) root of 'memory' '''
		try:					# Catch if passed value is Zero
			if b==None:
				c = pow(self.memory, 1/a)
			else:
				c = pow(a, 1/b)
			self.memory = c
			return (format(c, '.2f'))
		except ZeroDivisionError:
			return ("Division by 0")

	def reset(self):	
		'''Reset 'memory' to 0'''
		self.memory = 0
		return ("Reset done")


if __name__ == "__main__":
	calculator = Calculator()
	print(calculator.add(3,5))
	print(calculator.add(1))
	print(calculator.reset())
	print(calculator.add(1))
	print(calculator.mul(5))
	print(calculator.add(1))
	print(calculator.nrt(-2))
	print(calculator.add(1))
	print(calculator.div(0))
	print(calculator.add(1,3))
	print(calculator.add(1))
