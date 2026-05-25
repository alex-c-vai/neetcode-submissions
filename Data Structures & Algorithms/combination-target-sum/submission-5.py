class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, stack, curr):
            if curr == target:
                res.append(stack.copy())
                return
            if i >= len(nums) or curr > target:
                return
            
            stack.append(nums[i])
            dfs(i, stack, curr+nums[i])
            stack.pop()
            dfs(i+1, stack, curr)
            return

        dfs(0, [], 0)
        return res