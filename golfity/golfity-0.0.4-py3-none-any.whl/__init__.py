from adicity import Adicity, Pointer, errors
from golfity.arrays import Array, expandarray, ensureArray
from golfity.lib.standard import GolfityStandard
import sys

Golfity = Adicity('Golfity', '*')

# Namespaces stuff
Golfity.namespacesep(r'`(.*?)`')

# Other libraries
Golfity.add_language(GolfityStandard)
# Golfity.add(GolfityStandard)
# Golfity.add(GolfityStandard)

# Nulls
Golfity.ignore(r'\s')
Golfity.ignore(r'[\(\)]')
Golfity.ignore(r'\n')
Golfity.ignore(r',')
Golfity.ignore(r'".*?"')
Golfity.ignore(r'^".*?$')



@Golfity.totype
def to_array(value):
	if isinstance(value, int):
		return Array(value)
	elif isinstance(value, (str, float)):
		return Array(value)
	elif isinstance(value, Array):
		return value
	else:
		return Array(*value)

class SkipIteration(Exception):
	"""This Exception is raised on a 'continue' statement in the Golfity language."""
	pass

Golfity.token(r'\+', custom_name='ADDITION')(lambda a, b: a + b)
Golfity.token(r'-', custom_name='SUBTRACTION')(lambda a, b: a - b)
Golfity.token(r'\*', custom_name='MULTIPLICATION')(lambda a, b: a * b)
Golfity.token(r'/', custom_name='DIVISION')(lambda a, b: a / b)
Golfity.token(r'%', custom_name='MODULUS')(lambda a, b: a % b)
Golfity.token(r'^', custom_name='EXPONENTATION')(lambda a, b: a ** b)



@Golfity.token(r'x([a-f0-9]+)')
def HEX_INTEGER(self):
	"""An integer in (lowercase) hex format."""
	return Array(int(self.capture, 16))


@Golfity.token(r'-?[0-9]+\.[0-9]+')
def FLOAT(self):
	"""A floating point decimal number."""
	return float(self.capture)


@Golfity.token(r'-?[0-9]+')
def INTEGER(self):
	"""A base 10 signed integer."""
	return int(self.capture, 10)


@Golfity.token(r"'(.*?)'")
def STRING(self):
	"""A string literal, single quotes only. No escapes."""
	return Array(*map(ord, self.capture))


@Golfity.token(r'[A-Z]')
def VARIABLE(self):
	"""A variable."""
	result = Golfity.getvar(self.capture)
	return 0 if result is None else result



@Golfity.token(r'\[', end=r'\]')
def ARRAY(self):
	items = []
	for arg in self.args:
		val = arg()
		if len(val) == 1:
			items += val.items
		else:
			items.append(val)
	return Array(*items)

@Golfity.token(r'\{', end=r'\}')
def BLOCK(self):
	out = 0
	for arg in self.args:
		out = arg()
	return out

@Golfity.token(r'[^\x00-\x7F]+')
def DATA(self):
	return bytes(self.capture.encode())

# @Golfity.token(r'`', custom_name='DEBUG_DUMP')
# def DEBUG_DUMP(self):
# 	PROGRAM.pretty()
# 	return 0

# @Golfity.token(r'~', custom_name='BREAKPOINT')
# def DEBUG_LINE(self):
#	 pass


@Golfity.token(r'!')
def NOT(value):
	return int(not bool(value))


@Golfity.token(r'\|')
def OR(value1, value2):
	return int(bool(value1) or bool(value2))


@Golfity.token(r'&')
def AND(a, b):
	return int(bool(a) and bool(b))


@Golfity.token(r'=')
def EQUALITY(a, b):
	return int(a == b)


@Golfity.token(r'>')
def MORETHAN(a, b):
	return int(a > b)


@Golfity.token(r'\$')
def ECHO_NEWLINE(self, value):
	"""
	Prints the Unicode values of $1 to stdout with a trailing newline.
	This is equivalent to ECHO_OLDLINE, but with a newline at the end.
	"""
	ECHO_OLDLINE(self, value)
	print()


@Golfity.token(r';')
def ECHO_OLDLINE(self, value):
	"""
	Prints the Unicode values of $1 to stdout with no trailing newline.
		-   $1: Unicode values to be printed, these are expanded.
	"""
	try:
		print("".join(map(chr, expandarray(value))), end="")
	except ValueError:
		raise errors.InvalidAdicityCharacter(self)
	return 0


@Golfity.token(r'#')
def TO_STR(value):
	str_value = str(value)
	if len(value.items) == 1:
		str_value = str_value[1:-1]
	return Array(*map(ord, str_value))


@Golfity.token(r':')
def RANGE(lower_bound, upper_bound):
	out = Array()
	out.items = []
	for i in range(lower_bound, upper_bound + 1):
		out.append(i)
	return out


@Golfity.token(r'\?')
def IF(condition, then: Pointer, otherwise: Pointer):
	if bool(condition):
		return then()
	else:
		return otherwise()


@Golfity.token(r'@')
def WHILE_LOOP(condition: Pointer, counter: Pointer, work: Pointer):
	count = 0
	out = Array()
	out.items = []
	while condition():
		try:
			Golfity.setvar(counter.capture, count)
			out.append(work())
			count += 1
		except SkipIteration:
			continue
		except StopIteration:
			break
	return out


@Golfity.token(r'<')
def INPUT(_type):
	index = int(_type)
	argv = sys.argv[1:]
	if index == 0:
		return Array(input('DEBUG REMOVE ME!! (input) > '))
	try:
		return [
			Array(*argv),
			Array(0)
		][index - 1]
	except IndexError:
		return 0



@Golfity.token(r'\\')
def CONSTANTS(index):
	items = [
		Array("Hello, World!"),
		Array("Fizz"),
		Array("Buzz"),
		Array("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067"),
		Array("FizzBuzz"),
		Array(0)
	]
	try:
		return items[index]
	except IndexError:
		return 0


@Golfity.token(r'\.')
def INCREMENT(variable: Pointer):
	return Golfity.setvar(variable.capture, variable() + 1)


@Golfity.token(r'_')
def DECREMENT(variable: Pointer):
	return Golfity.setvar(variable.capture, variable() - 1)


Golfity.default_namespace = '_'
