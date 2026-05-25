class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for c in s:
            if c in closing:
                stack.append(c)
            else:
                if stack and c == closing[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0