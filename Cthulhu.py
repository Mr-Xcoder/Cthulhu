class properties(dict):
	def __init__(self, *args, **kwargs):
		dict.__init__(self, *args, **kwargs)
		self.__dict__ = self

functions = {

    # Operator Functions

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

    # Operators with Precedence of 3 (Irrelevant in Cthulhu, but a nice sorting criterion)

    '^' : properties(

        # Raise the first value to the power of the second value

        arity = 2,
        function = lambda a,b: a ** b

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

    '>': properties(

        # Check if the first value is higher than the second value

        arity = 2,
        function = lambda a,b: a > b

    ),

    '≤': properties(

        # Check if the first value is smaller than or equal to the second value

        arity = 2,
        function = lambda a,b: a <= b

    ),

    '≥': properties(

        # Check if the first value is greater than or equal to the second value

        arity = 2,
        function = lambda a,b: a >= b

    ),

    # Standard functions

    'ª' : properties(
        arity = 2,
        function = list.append
    ),
    'º' : properties(
        arity = 2,
        function = lambda array,ommited_index:list([array[index] for index in range(len(array)) if index != ommited_index])
    ),
    '¬' : properties(
        arity = 1,
        function = len
    )
}