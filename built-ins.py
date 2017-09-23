import math

def increment(a):
    if isinstance(a, int) or isinstance(a, float):
        return a + 1
    elif isinstance(a, list):
        return [increment(x) for x in a]
    return "".join(map(lambda x: chr(ord(x) + 1), a))


def decrement(a):
    if isinstance(a, int) or isinstance(a, float):
        return a - 1
    elif isinstance(a, list):
        return [decrement(a) for x in a]
    return "".join(map(lambda x: chr(ord(x) - 1), a))


def double(a):
    if isinstance(a, int) or isinstance(a, float):
        return a * 2
    elif isinstance(a, list):
        return [double(x) for x in a]
    return "".join(map(lambda x: chr(ord(x) * 2), a))


def halve(a):
    if isinstance(a, int) or isinstance(a, float):
        return a / 2
    elif isinstance(a, list):
        return [halve(x) for x in a]
    return "".join(map(lambda x: chr(ord(x) / 2), a))


def square(a):
    if isinstance(a, list):
        return [square(x) for x in a]
    return a ** 2


def square_root(a):
    if isinstance(a, list):
        return [square_root(x) for x in a]
    return math.sqrt(a)


def add(a, b):
    if isinstance(a, list) and (isinstance(b, float) or isinstance(b, int)):
        return [x + b for x in a]
    elif isinstance(b, list) and (isinstance(a, float) or isinstance(a, int)):
        return [x + a for x in b]
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) > len(b):
            return [x + y for x, y in zip(b + [1] * (len(a) - len(b)), a)]
        elif len(b) > len(a):
            return [x + y for x, y in zip(a + [1] * (len(b) - len(a)), b)]
        return [x + y for x,y in zip(a, b)]
    return a + b


def subtract(a, b):
    if isinstance(a, list) and (isinstance(b, float) or isinstance(b, int)):
        return [x - b for x in a]
    elif isinstance(b, list) and (isinstance(a, float) or isinstance(a, int)):
        return [x - a for x in b]
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) > len(b):
            return [x - y for x, y in zip(b + [1] * (len(a) - len(b)), a)]
        elif len(b) > len(a):
            return [x - y for x, y in zip(a + [1] * (len(b) - len(a)), b)]
        return [x - y for x,y in zip(a, b)]
    return a - b

def multiply(a, b):
    if isinstance(a, list) and (isinstance(b, float) or isinstance(b, int)):
        return [x * b for x in a]
    elif isinstance(b, list) and (isinstance(a, float) or isinstance(a, int)):
        return [x * a for x in b]
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) > len(b):
            return [x * y for x, y in zip(b + [1] * (len(a) - len(b)), a)]
        elif len(b) > len(a):
            return [x * y for x, y in zip(a + [1] * (len(b) - len(a)), b)]
        return [x * y for x,y in zip(a, b)]
    return a * b


def divide(a, b):
    if isinstance(a, list) and (isinstance(b, float) or isinstance(b, int)):
        return [x / b for x in a]
    elif isinstance(b, list) and (isinstance(a, float) or isinstance(a, int)):
        return [x / a for x in b]
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) > len(b):
            return [x / y for x, y in zip(b + [1] * (len(a) - len(b)), a)]
        elif len(b) > len(a):
            return [x / y for x, y in zip(a + [1] * (len(b) - len(a)), b)]
        return [x / y for x,y in zip(a, b)]
    return a / b


def integer_divide(a, b):
    if isinstance(a, list) and (isinstance(b, float) or isinstance(b, int)):
        return [x // b for x in a]
    elif isinstance(b, list) and (isinstance(a, float) or isinstance(a, int)):
        return [x // a for x in b]
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) > len(b):
            return [x // y for x, y in zip(b + [1] * (len(a) - len(b)), a)]
        elif len(b) > len(a):
            return [x // y for x, y in zip(a + [1] * (len(b) - len(a)), b)]
        return [x // y for x,y in zip(a, b)]
    return a // b


def exponentiation(a, b):
    if isinstance(a, list) and (isinstance(b, float) or isinstance(b, int)):
        return [x ** b for x in a]
    elif isinstance(b, list) and (isinstance(a, float) or isinstance(a, int)):
        return [x ** a for x in b]
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) > len(b):
            return [x ** y for x, y in zip(b + [1] * (len(a) - len(b)), a)]
        elif len(b) > len(a):
            return [x ** y for x, y in zip(a + [1] * (len(b) - len(a)), b)]
        return [x ** y for x,y in zip(a, b)]
    return a ** b


def root(a, b):
    if isinstance(a, list) and (isinstance(b, float) or isinstance(b, int)):
        return [x ** (1 / b) for x in a]
    elif isinstance(b, list) and (isinstance(a, float) or isinstance(a, int)):
        return [x ** (1 / a) for x in b]
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) > len(b):
            return [x ** (1 / y) for x, y in zip(b + [1] * (len(a) - len(b)), a)]
        elif len(b) > len(a):
            return [x ** (1 / y) for x, y in zip(a + [1] * (len(b) - len(a)), b)]
        return [x ** (1 / y) for x,y in zip(a, b)]
    return a ** (1 / b)
