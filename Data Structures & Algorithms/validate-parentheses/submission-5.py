class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openPar = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for c in s:
            if c in openPar.keys():
                stack.append(c)
            else:
                if stack and c == openPar[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0