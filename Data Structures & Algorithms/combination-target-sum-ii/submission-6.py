class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, stack, curr):
            if curr == target:
                res.append(stack.copy())
                return
            if i >= len(candidates) or curr > target:
                return
            stack.append(candidates[i])
            backtrack(i+1, stack, curr+candidates[i])
            stack.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, stack, curr)
            return
        
        backtrack(0, [], 0)
        return res