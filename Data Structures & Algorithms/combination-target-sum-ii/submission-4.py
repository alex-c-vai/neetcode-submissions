class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i, curr, stack):
            if curr == target:
                res.append(stack.copy())
                return
            if curr > target or i >= len(candidates):
                return
            
            # in this backtracking variant
            # our decision tree is either to keep or skip
            # instead of possible reusing each elem multiple times
            stack.append(candidates[i])
            backtrack(i+1, curr+candidates[i], stack)
            stack.pop()
            # this while loop ensures we don't use duplicates:
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, curr, stack)
            return
        
        backtrack(0, 0, [])
        return res
