class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # for each index we have two option: take it or skip and move on

        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
        
        dfs(0, [])
        return res