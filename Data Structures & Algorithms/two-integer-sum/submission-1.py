class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compMap = dict()

        for i, n in enumerate(nums):
            if n in compMap:
                return [compMap[n], i]
            compMap[target-n] = i
        
        return