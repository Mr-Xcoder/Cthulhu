import sympy
import math
import sys

pause = 0
stack = []
STDIN = []
register_1 = []
register_2 = []
digits = "0123456789"

if "--input" in sys.argv[1:]:
    STDIN = open("input.txt", "r").read().split("\n")

else:
    STDIN = sys.stdin.read().split("\n")


class Command:
    global stack
    arity: int = 0
    func: callable = None
    is_void: bool = False
    neutral_elements: list = []

    def __init__(self, arity: int, func: callable, is_void: bool = False, neutral_elements: list = []):
        self.arity = arity
        self.func = func
        self.is_void = is_void
        self.neutral_elements = neutral_elements

    def call(self):
        argument_list = []
        for i in range(self.arity):
            try:
                argument_list = [stack.pop()] + argument_list
            except IndexError:
                argument_list.append(self.neutral_elements.pop(0) if self.neutral_elements else 0)
        if self.is_void:
            self.func(*argument_list)
        else:
            stack.append(self.func(*argument_list))


def primefac(x: int) -> list:
    result = []
    for factor, exponent in sympy.ntheory.factor_.factorint(int(x)).items():
        result.extend([factor] * exponent)
    return result


def wrap_stack():
    global stack
    stack = [stack]


def evaluate(x: object) -> object:
    try:
        return eval(x)
    except (ValueError, SyntaxError):
        return x


commands = {
    # Bifunctions
    '+': Command(2, (lambda x, y: x + y), neutral_elements=[0, 0]),
    '-': Command(2, (lambda x, y: x - y), neutral_elements=[0, 0]),
    '/': Command(2, (lambda x, y: x / y), neutral_elements=[1, 1]),
    '*': Command(2, (lambda x, y: x * y), neutral_elements=[1, 1]),
    'ˆ': Command(2, (lambda x, y: x ** y), neutral_elements=[1, 1]),
    '%': Command(2, (lambda x, y: x % y), neutral_elements=[1, 1]),
    ':': Command(2, (lambda x, y: x // y), neutral_elements=[1, 1]),
    '|': Command(2, (lambda x, y: x | y), neutral_elements=[1, 1]),
    'X': Command(2, (lambda x, y: x ^ y), neutral_elements=[1, 1]),
    '&': Command(2, (lambda x, y: x & y), neutral_elements=[1, 1]),
    '>': Command(2, (lambda x, y: int(x > y)), neutral_elements=[2, 1]),
    '<': Command(2, (lambda x, y: int(x < y)), neutral_elements=[0, 1]),
    '≥': Command(2, (lambda x, y: int(x >= y)), neutral_elements=[1, 1]),
    '≤': Command(2, (lambda x, y: int(x <= y)), neutral_elements=[1, 1]),
    '=': Command(2, (lambda x, y: int(x == y)), neutral_elements=[1, 1]),
    '≠': Command(2, (lambda x, y: int(x != y)), neutral_elements=[1, 1]),
    # Unifunctions
    ',': Command(1, (lambda x: [stack.pop(-1 if x >= 0 else 0) for _ in range(abs(x))
                                if stack][::-1 if x >= 0 else 1])),
    '_': Command(1, (lambda x: -x if isinstance(x, int) or isinstance(x, float) else x[::-1])),
    'p': Command(1, (lambda x: sympy.primetest.isprime(int(x)) if x >= 0 else primefac(abs(x))), neutral_elements=[1]),
    'd': Command(1, sympy.ntheory.factor_.divisors, neutral_elements=[1]),
    'I': Command(1, (lambda x: evaluate(STDIN[x]) if len(STDIN) > x else
                                [1024, sympy.pi, math.e, "aeiou", "bcdfghjklmnpqrstvwxyz"][x % 5])),
    'l': Command(1, str.lower, neutral_elements=["abcdefghijklmnopqrstuvwxyz"]),
    'u': Command(1, str.upper, neutral_elements=["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]),
    'e': Command(1, (lambda x: 10 ** x), neutral_elements=[3]),
    '±': Command(1, (lambda x: (x > 0) - (x < 0)), neutral_elements=[0]),
    '!': Command(1, (lambda x: 1-x)),
    # Invariant functions
    'i': Command(0, (lambda x: evaluate(STDIN[0]) if STDIN else 100)),
    'r': Command(0, (lambda x: STDIN[0] if STDIN else 2 ** 31 - 1)),
    # Stack manipulators
    's': Command(2, (lambda x, y: stack.extend([y, x])), is_void=True, neutral_elements=[0, 0]),
    'S': Command(3, (lambda x, y, z: stack.extend([z, y, x])), is_void=True, neutral_elements=[0, 0, 0]),
    'D': Command(1, (lambda x: stack.extend([x, x])), is_void=True, neutral_elements=[0]),
    'T': Command(1, (lambda x: stack.extend([x, x, x])), is_void=True, neutral_elements=[0]),
    'W': Command(0, wrap_stack, is_void=True)
}


def run(program):
    global pause
    global stack
    global STDIN
    global register_1
    global register_2

    for index, command in enumerate(program):

        # Handling Multi-Byte commands

        if pause:
            pause -= 1
            continue

        # Handling strings

        if command == '"' and (program[index - 1] != '\\' if index != 0 else True):
            if (program[:index].count('"') - program[:index].count('\\"')) % 2 == 0:
                stack.append("")

        elif (program[:index].count('"') - program[:index].count('\\"')) % 2:
            stack[-1] += command

        # Handling number literals, which are special functions

        elif command in digits:

            # Multi-digit integers
            if index != 0 and program[index - 1] in digits:
                stack[-1] = stack[-1] * 10 + int(command)
            # Pushing digits
            else:
                stack.append(int(command))

        else:
            if command in commands.keys():
                commands[command].call()

    return stack[-1]
