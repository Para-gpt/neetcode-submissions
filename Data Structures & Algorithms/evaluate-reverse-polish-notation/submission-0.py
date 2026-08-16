class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['+', '-', '*', '/']
        stack = []

        for i in tokens:
            if i in operands:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if i == '+':
                    res = num1 + num2
                elif i == '-':
                    res = num1 - num2
                elif i == '*':
                    res = num1 * num2
                elif i == '/':
                    res = int(num1 / num2)
                stack.append(res)

            else:
                stack.append(int(i))
        return stack.pop()

        