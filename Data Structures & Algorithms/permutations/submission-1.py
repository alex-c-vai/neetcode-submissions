class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, curr, pick):
            # end condition
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            # out of bounds condition
            if i == len(nums):
                return
            # for every single number
            for j in range(len(nums)):
                # if not already part of the permutation choose the number
                if pick[j] == False:
                    pick[j] = True
                    curr.append(nums[j])
                    backtrack(i+1, curr, pick)
                    curr.pop() # undo choice
                    pick[j] = False # undo choice
        
        backtrack(0, [], [False]*len(nums))
        return res