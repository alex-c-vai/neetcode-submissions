class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # memo, but also keeps track 2 states - first house robbed or not
        memo = [[-1]*2 for _ in range(len(nums))]
        
        # decision tree DP
        def dfs(i, flag):
            # we can't rob out of bounds or the last house when the first one was robbed
            if i >= len(nums) or (flag and i == len(nums)-1):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            memo[i][flag] = max(dfs(i+1, flag), nums[i]+dfs(i+2, flag or i==0))
            return memo[i][flag]
        
        return max(dfs(0, True), dfs(1, False))