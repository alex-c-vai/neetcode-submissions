class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for (i, n) in enumerate(nums):
            if i > 0 and n == nums[i-1]: continue
            l = i+1
            r = len(nums) - 1
            while l < r and l < len(nums) and r > 0:
                total = n + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res