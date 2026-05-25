class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 1
        prefix = {}
        suffix = {}

        for (i, n) in enumerate(nums):
            prefix[i] = curr * n
            curr = curr * n
        
        curr = 1
        for j in range(len(nums)-1, -1, -1):
            suffix[j] = curr * nums[j]
            curr = curr * nums[j]
        
        res = []

        for i in range(len(nums)):
            p = prefix[i-1] if i > 0 else 1
            s = suffix[i+1] if i < len(nums)-1 else 1
            res.append(s * p)
        return res