class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total): 
            # if we reached our target then stop and append this to the result
            if total == target:
                res.append(cur.copy())
                return
            # if we are out of bounds or exceeded target then prune this path
            if i >= len(nums) or total > target:
                return

            # backtrack
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res