class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            stack.append(tokens[i])
            print(stack)
            if tokens[i] == '+':
                val = int(stack[-3]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(val)
            elif tokens[i] == '-':
                val = int(stack[-3]) - int(stack[-2])
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(val)
            elif tokens[i] == '*':
                val = int(stack[-3]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(val)
            elif tokens[i] == '/':
                val = int(int(stack[-3]) / int(stack[-2]))
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append(val)
        return int(stack[0])