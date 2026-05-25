class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+", "-", "*", "/"]

        for token in tokens:
            if token not in operands:
                sign = 1
                if token[0] == "-":
                    sign = -1
                    token = token[1:]
                number = sign * int(token)
                stack.append(number)
            else:
                print(stack)
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(second - first)
                elif token == "*":
                    stack.append(first * second)
                elif token == "/":
                    stack.append(int(second / first))
        
        return stack[0]