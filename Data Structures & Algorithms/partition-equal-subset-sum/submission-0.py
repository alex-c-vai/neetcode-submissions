class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum%2 == 1: return False
        t = totalSum // 2
        memo = [[-1] * (t+1) for _ in range(len(nums))]
        def dfs(i, target):
            if target == 0:
                return True
            if i == len(nums) or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            memo[i][target] = dfs(i+1, target) or dfs(i+1, target-nums[i])
            return memo[i][target]
        
        return dfs(0, t)