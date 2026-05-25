class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr, val):
            print(curr)
            if val == target:
                res.append(curr.copy())
                return
            if i == len(candidates) or val > target:
                return
            
            # take or skip the current index
            curr.append(candidates[i])
            dfs(i+1, curr, val + candidates[i])
            curr.pop()
            
            # this is the trick for this problem; after sorting we need to skip identical indexes
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, curr, val)

        dfs(0,[],0)
        return res