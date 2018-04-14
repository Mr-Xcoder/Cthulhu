stack = []

code_page = '''¡¢£§¥•©¬®µ∞¿€ÆÇ∂˜°ØŒεßæç¨ªº√÷øœ™ !"#$%&'()*+,-./0123456789:;<=>?''' \
            '''@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¶''' \
            '''≥≤…˘¯˙åÅàÀáÁäÄãÃāĀèÈéÉêÊëËēĒėĖęĘîÎïÏíÍīĪįĮìÌôÔöÖòÒóÓoōŌõÕûÛüÜùÙú''' \
            '''ÚūŪƒﬁﬂ‡†›‹⁄◊´‰ˇˆπ∏ı∫ńŃñÑÿŸśŚšŠłŁžŽźŹżŻćĆčČńŃ»«“”‘’∑≈Ω–—\nΛλ¶∊≟∆δ'''


class Command:
    global stack
    arity: int = 0
    func: callable = None
    is_void: bool = False
    neutral_elements: list = []

    def __init__(self, arity: int, func: callable, is_void: bool = False, neutral_elements: tuple = ()):
        self.arity = arity
        self.func = func
        self.is_void = is_void
        self.neutral_elements = list(neutral_elements)

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
