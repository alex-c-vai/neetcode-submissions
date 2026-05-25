class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, total, stack):
            if total == target:
                res.append(stack.copy())
                return
            if i>=len(candidates) or target < total:
                return
            # this doesn't ensure uniqueness; how do I solve this?
            stack.append(candidates[i])
            dfs(i+1, total+candidates[i], stack)
            stack.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total, stack)
        
        dfs(0, 0, [])
        return res