class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []
        def backtrack(i, stack):
            if len(stack) == len(digits):
                res.append("".join(stack.copy()))
                return
            print(len(stack))
            for c in nums[digits[i]]:
                stack.append(c)
                backtrack(i+1, stack)
                stack.pop()
            
        if digits:
            backtrack(0, [])
        return res