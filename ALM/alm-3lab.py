class Calculator:
    def __init__(self, expression):
        self.expression = expression
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['(', ')', ' ']
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2}
        self.output = []
        self.elements = []
        self.__pols()

    def parse_expression(self):

        element = ''
        elements = []

        for i in range(len(self.expression)):
            char = self.expression[i]

            if char in self.operators:
                if element != '':
                    elements.append(element)
                elements.append(char)
                element = ''
            elif char in self.digits:
                element += char
            elif char == '(' or char == ')':
                if element != '':
                    elements.append(element)
                    element = ''
                elements.append(char)
                continue
            elif char == ' ':
                continue

        if element:
            elements.append(element)

        return elements

    def __pols(self):
        self.elements = self.parse_expression()

        stack = []
        for element in self.elements:
            if element.isdigit():
                self.output.append(element)
            elif element in self.operators:
                while stack and self.operators.get(stack[-1], 0) >= self.operators.get(element, 0):
                    self.output.append(stack.pop())
                stack.append(element)
            elif element == '(':
                stack.append(element)
            elif element == ')':
                while stack and stack[-1] != '(':
                    self.output.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()

        while stack:
            self.output.append(stack.pop())

    def check_expression(self):
        print("S11->", end="")
        for i in self.expression:  # x9
            if not (i in self.digits or i in self.symbols or i in self.operators):  # x10
                print("S12->", end="")
                print("S11->", end="")
                return False  # y13
        for element in self.elements:  # x11
            if element.isdigit() and not (0 <= int(element) <= 65535):  # x12
                print("S13->", end="")
                print("S11->", end="")
                return False  # y13

        if '' in self.elements:  # x13
            print("S14->", end="")
            print("S11->", end="")
            return False  # y13

        stack = []  # y1
        print("S15->", end="")
        for element in self.elements:  # x11
            if element == '(':  # x14
                stack.append(element)  # y14
                print("S16->", end="")
            elif element == ')':  # x15
                if not stack or stack[-1] != '(':  # x16
                    print("S17->", end="")
                    print("S11->", end="")
                    return False  # y13
                print("S18->", end="")
                stack.pop()  # y15

        if stack:  # x17
            print("S22->", end="")
            print("S11->", end="")
            return False  # y13

        output = self.output  # y16
        print("S19->", end="")
        for element in output:  # x18
            if element.isdigit():  # x19
                continue
            elif element in self.operators:  # x20
                if len(output) < 2:  # x21
                    print("S20->", end="")
                    print("S11->", end="")
                    return False  # y13
            else:
                print("S21->", end="")
                print("S11->", end="")
                return False  # y13
        print("S23->", end="")
        print("S11->", end="")
        return True  # y17

    def count(self):
        print("S0->", end="")
        stack = []  # y1
        print("S1->", end="")
        for element in self.output:  # x1
            if element.isdigit():  # x2
                stack.append(int(element))  # y2
                print("S2->", end="")
            elif element in self.operators:  # x3
                operand2 = stack.pop()  # y3
                operand1 = stack.pop()  # y4
                print("S3->", end="")
                if element == '+':  # x4
                    stack.append(operand1 + operand2)  # y5
                    print("S4->", end="")
                elif element == '-':  # x5
                    stack.append(operand1 - operand2)  # y6
                    print("S5->", end="")
                elif element == '*':  # x6
                    stack.append(operand1 * operand2)  # y7
                    print("S6->", end="")
                elif element == '/':  # x7
                    stack.append(round(operand1 / operand2))  # y8
                    print("S7->", end="")
        main_result = stack.pop()  # y9
        print("S8->")
        if main_result > 65535 or main_result < 0:  # x8
            print("S9->")
            print("Результат вышел за пределы [0,65535]")  # y10
            print("S0->", end="")
            return 0  # y11
        print("S10->", end="")
        print("S0->", end="")
        return main_result  # y12


if __name__ == "__main__":
    a = Calculator("1 * 65534 + 20/2) - 10 + 1")
    allowed = a.check_expression()
    print()
    print(allowed)
    if allowed:
        result = a.count()
        print()
        print(a.expression, '=', result)
