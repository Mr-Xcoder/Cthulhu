import math, string
fib_cache = {0:0, 1:1, 2:1}

class properties(dict):
	def __init__(self, *args, **kwargs):
		dict.__init__(self, *args, **kwargs)
		self.__dict__ = self

def is_fibonacci(a):n = (.5 + .5 * 5.0 ** .5) * a;return a == 0 or abs(round(n) - n) < 1.0 / a

def Fib(n):
	global fib_cache
	if n in fib_cache:
		return fib_cache[n]
	else:
		result = ath_fibonacci(n)[1]
		fib_cache[n] = result
		return result

def ath_fibonacci(n):
	global fib_cache
	if n==0: return 1,0
	shift = n>>1
	if shift in fib_cache and shift-1 in fib_cache:
		a,b = fib_cache[shift-1],fib_cache[shift]
	else:
		a,b = ath_fibonacci(shift)
		fib_cache[shift-1] = a
		fib_cache[shift] = b
	b2 = b*b
	a,b = a*a+b2, (a<<1)*b+b2
	if n%2 == 1:
		fib_cache[n-1] = b
		return b,a+b
	fib_cache[n-1] = a
	return a,b

def first_a_fibonacci(a):
	result = []
	if a<0: return []
	elif a<3: return [0,1,1][:a]
	else:
		x,y = 0,1
		result += [x,y]
		while a-2>=0:x,y=y,x+y;a-=1;result.append(y)
		return result

functions = {

	# OPERATOR FUNCTIONS
	# Operators with a precendece of 1 (Irrelevant in Cthulhu, but a nice sorting criterion)

	'+' : properties(
		# Addition
		arity = 2,
		function = lambda a,b: a + b
	),
	'-' : properties(
		# Subtraction
		arity = 2,
		function = lambda a,b: a - b
	),
	'#' : properties(
		# Absolute Difference
		arity = 2,
		function = lambda a,b: abs(a - b)
	),
	'±' : properties(
		# Solve both Adittion and Sutraction, returns a tuple with the first value being the sum and the other one the difference
		arity = 2,
		function = lambda a,b: (a + b, a - b)
	),

	# Operators with Precedence of 2 (Irrelevant in Cthulhu, but a nice sorting criterion)
	'*' : properties(
		# Multiplication
		arity = 2,
		function = lambda a,b: a * b
	),
	'/' : properties(
		# Division
		arity = 2,
		function = lambda a,b: a / b
	),
	'÷' : properties(
		# Integer division
		arity = 2,
		function = lambda a,b: a // b
	),
	'%' : properties(
		# Modulo
		arity = 2,
		function = lambda a,b: a % b
	),

	# Operators with Precedence of 3 (Irrelevant in Cthulhu, but a nice sorting criterion)
	'^' : properties(
		# Raise the first value to the power of the second value
		arity = 2,
		function = lambda a,b: a ** b
	),
	'√' : properties(
		# Generic Root
		arity = 2,
		function = lambda a,b: a ** (1/b)
	),
	'²' : properties(
		# Square an integer
		arity = 1,
		function = lambda a: a ** 2
	),
	'◊' : properties(
		# Square Root
		arity = 1,
		function = lambda a: a ** 0.5
	),

	# Comparison Operators
	'=' : properties(
		# Check if the values provided are equal
		arity = 2,
		function = lambda a,b: a == b
	),
	'≠' : properties(
		# Check if the values provided are not equal
		arity = 2,
		function = lambda a,b: a != b
	),
	'<' : properties(
		# Check if the first value is smaller than the second value
		arity = 2,
		function = lambda a,b: a < b
	),
	'>' : properties(
		# Check if the first value is higher than the second value
		arity = 2,
		function = lambda a,b: a > b
	),
	'≤' : properties(
		# Check if the first value is smaller than or equal to the second value
		arity = 2,
		function = lambda a,b: a <= b
	),
	'≥' : properties(
		# Check if the first value is greater than or equal to the second value
		arity = 2,
		function = lambda a,b: a >= b
	),

	# Boolean Operators
	'&' : properties(
		# Logical AND
		arity = 2,
		function = lambda a,b: a and b
	),
	'|' : properties(
		# Logical OR
		arity = 2,
		function = lambda a,b: a or b
	),
	'¬' : properties(
		# Logical NOT
		arity = 1,
		function = lambda a: not a
	),

	# Bitwise Operators
	'~' : properties(
		# The Bitwise Complement
		arity = 1,
		function = lambda a: ~a
	),
	'⪡' : properties(
		# Shifts the bits to the left
		arity = 2,
		function = lambda a,b: a << b
	),
	'⪢' : properties(
		# Shifts the bits to the right
		arity = 2,
		function = lambda a,b: a >> b
	),
	'¢' : properties(
		# Bitwise AND
		arity = 2,
		function = lambda a,b: a & b
	),
	'º' : properties(
		# Bitwise OR
		arity = 2,
		function = lambda a,b: a | b
	),
	'ˆ' : properties(
		# Bitwise XOR
		arity = 2,
		function = lambda a,b: a ^ b
	),

	# Sequence Built-ins
	'ﬁ' : properties(
		# Checks if the given number is a Fibonacci number
		arity = 1,
		function = is_fibonacci
	),
	'ﬂ' : properties(
		# Returns the a-th Fibonacci number (0-indexed): `0 -> 0, 1-> 1, 2 -> 1, 3 -> 2, 4 -> 3, 5 -> 5, 6 -> 8...`
		arity = 1,
		function = ath_fibonacci
	),
	'ƒ' : properties(
		arity = 1,
		function = first_a_fibonacci
	),
	# List operations
	'…' : properties(
		# Range
		arity = 2,
		function = range
	),
	'@' : properties(
		# Array index.
		# First argument is the list,
		# Second is a zero-based index.
		arity = 2,
		function = lambda x,y: x[y]
	)
}
constants = {
	'D' : 0.5,
	'Z' : 0,
	'O' : 1,
	'F' : 5,
	'E' : 10,
	'W' : 20,
	'Y' : 50,
	'H' : 100,
	'T' : 1000,
	'M' : 1000000,
	# Mathematical Constants
	'π' : math.pi,
	'ϕ' : 1.6180339887,
	'γ' : 0.5772156649,
	'e' : math.e,
	'δ' : 4.6692,
	'α' : 2.5029,
	'j' : 1j,
	# String Constants
	'n' : '\n',
	's' : ' ',
	'g' : '',
	'Î' : string.digits,
	'å' : 'abcdefghijklmnopqrstuvwxyz',
	'Å' : 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
	'Ø' : string.printable
}
