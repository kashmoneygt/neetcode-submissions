class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                a, b = stack.pop(), stack.pop()
                if token == "+": stack.append(a + b)
                elif token == "*": stack.append(a * b)
                elif token == "/": stack.append(int(b / a))
                elif token == "-": stack.append(b - a)
            else:
                stack.append(int(token))
        
        return stack[0]