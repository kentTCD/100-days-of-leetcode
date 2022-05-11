class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for t in tokens:
            # print(stack)
            if t not in operators:
                stack.append(t)
            else:
                val = 0
                if t == '/':
                    val = math.trunc(int(stack[-2])/int(stack[-1]))
                elif t == '*':
                    val = int(stack[-2]) * int(stack[-1])
                elif t == '+':
                    val = int(stack[-2]) + int(stack[-1])
                elif t == '-':
                    val = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)
        return stack[0]