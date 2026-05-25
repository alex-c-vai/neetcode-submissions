class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr, stack):
            # if we reach our target it means we have a valid array
            if curr == target:
                res.append(stack.copy())
                return
            # if we go out of bounds we stop
            if curr>target or i >= len(nums):
                return
            
            # decision tree: use the current number or skip to the next
            stack.append(nums[i])
            backtrack(i, curr+nums[i], stack)
            stack.pop()
            backtrack(i+1, curr, stack)
            return

        backtrack(0, 0, [])
        return res