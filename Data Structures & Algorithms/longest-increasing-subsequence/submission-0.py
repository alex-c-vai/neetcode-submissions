class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            LIS = 1

            for j in range(i+1, len(nums), 1):
                if nums[i] < nums[j]:
                    LIS = max(LIS, 1 + dfs(j))
            memo[i] = LIS
            return memo[i]
        
        return max(dfs(k) for k in range(len(nums)))
            

            