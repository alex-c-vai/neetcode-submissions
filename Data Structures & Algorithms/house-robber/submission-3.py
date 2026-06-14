class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return nums[i]
            if memo[i] != -1:
                return memo[i]
            odd = dfs(i+1) # skip
            even = nums[i] + dfs(i+2) # rob
            memo[i] = max(odd, even)
            return memo[i]
        
        return dfs(0)