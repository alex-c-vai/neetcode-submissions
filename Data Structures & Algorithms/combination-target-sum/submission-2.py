class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, stack):
            if total == target:
                res.append(stack.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            stack.append(nums[i])
            dfs(i, total+nums[i], stack)
            stack.pop()
            dfs(i+1, total, stack)
        
        dfs(0, 0, [])
        return res