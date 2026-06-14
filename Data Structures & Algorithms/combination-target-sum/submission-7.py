class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, stack, curr):
            if i >= len(nums) or curr > target:
                return
            if curr == target:
                res.append(stack.copy())
                return
            stack.append(nums[i])
            backtrack(i, stack, curr+nums[i])
            stack.pop()
            backtrack(i+1, stack, curr)
            return

        backtrack(0, [], 0)
        return res
