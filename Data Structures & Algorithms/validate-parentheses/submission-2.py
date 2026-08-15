class Solution:
    def isValid(self, s: str) -> bool:
        ref = {')':'(', ']':'[', '}':'{'}

        stack = []

        for i in s:
            if i in ref:
                if stack and stack[-1] == ref[i]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(i)

        if not stack:
            return True
        else:
            return False

        