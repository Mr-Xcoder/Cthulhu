class properties(dict):
	def __init__(self, *args, **kwargs):
		dict.__init__(self, *args, **kwargs)
		self.__dict__ = self

def is_fibonacci(a):n = (.5 + .5 * 5.0 ** .5) * a;return a == 0 or abs(round(n) - n) < 1.0 / a

def athFibonacci(a):
	if a < 1: return 0
	elif a < 3: return 1
	else:
		x,y = 0,1
		while a-2>=0:x,y=y,x+y;a-=1

def first_a_fibonacci(a):
	result = []
	if a < 0: return []
	if a < 3: return [0,1,1][:a]
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
	'¡' : properties(
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
	'«' : properties(
		# Shifts the bits to the left
		arity = 2,
		function = lambda a,b: a << b
	),
	'»' : properties(
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
		# Checks if the given number is a Finonacci number
		arity = 1,
		function = is_fibonacci
	),
	'ﬂ' : properties(
		# Returns the a-th Fibonacci number (0-indexed): `0 -> 0, 1-> 1, 2 -> 1, 3 -> 2, 4 -> 3, 5 -> 5, 6 -> 8...`
		arity = 1,
		function = athFibonacci
	),
    	'ƒ' : properties(
		# Returns the first a Fibonacci numbers
        	arity = 1,
       		function = first_a_fibonacci
    	)
}
