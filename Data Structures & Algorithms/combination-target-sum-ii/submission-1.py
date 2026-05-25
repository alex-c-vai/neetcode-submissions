class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, stack, total):
            if total == target:
                res.append(stack.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            stack.append(candidates[i])
            backtrack(i+1, stack, total+candidates[i])
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            stack.pop()
            backtrack(i+1, stack, total)

        backtrack(0, [], 0)
        return res