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


def wrap_stack():
    global stack
    stack = [stack]


commands = {
    # Bifunctions
    '+': Command(2, (lambda x, y: x + y), neutral_elements=[0, 0]),
    '-': Command(2, (lambda x, y: x - y), neutral_elements=[0, 0]),
    '/': Command(2, (lambda x, y: x / y), neutral_elements=[1, 1]),
    '*': Command(2, (lambda x, y: x * y), neutral_elements=[1, 1]),
    'ˆ': Command(2, (lambda x, y: x ** y), neutral_elements=[1, 1]),
    '%': Command(2, (lambda x, y: x % y), neutral_elements=[1, 1]),
    ':': Command(2, (lambda x, y: x // y), neutral_elements=[1, 1]),
    # Unifunctions
    ',': Command(1, (lambda x: [stack.pop(-1 if x >= 0 else 0) for _ in range(abs(x)) if stack][::-1 if x >= 0 else 1])),
    '_': Command(1, (lambda x: -x if isinstance(x, int) or isinstance(x, float) else x[::-1])),
    # Stack manipulators
    's': Command(2, (lambda x, y: stack.extend([y, x])), is_void=True, neutral_elements=[0, 0]),
    'S': Command(3, (lambda x, y, z: stack.extend([z, y, x])), is_void=True, neutral_elements=[0,0,0]),
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

        if command == '"' and (program[index-1] != '\\' if index != 0 else True):
            if (program[:index].count('"') - program[:index].count('\\"')) % 2 == 0:
                stack.append("")

        elif (program[:index].count('"') - program[:index].count('\\"')) % 2:
            stack[-1] += command

        # Handling number literals, which are special functions

        elif command in digits:

            # Multi-digit integers
            if index != 0 and program[index-1] in digits:
                stack[-1] = stack[-1] * 10 + int(command)
            # Pushing digits
            else:
                stack.append(int(command))

        else:
            if command in commands.keys():
                commands[command].call()

    return stack[-1]
