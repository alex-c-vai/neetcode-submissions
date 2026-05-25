class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, curr, pick):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            if i == len(nums):
                return
            
            for j in range(len(nums)):
                if pick[j] == False:
                    pick[j] = True
                    curr.append(nums[j])
                    backtrack(i+1, curr, pick)
                    curr.pop()
                    pick[j] = False
        
        backtrack(0, [], [False]*len(nums))
        return res