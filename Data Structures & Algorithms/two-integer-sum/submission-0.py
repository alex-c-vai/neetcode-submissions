class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        [4,5,6]
        10
        {6: 0, 5: 1, }
        for (i, num) in enumerate(nums):
            diff = target - num
            print(diff)
            if num in complements.keys():
                return [complements[num], i]
            else:
                complements[diff] = i
        
        return []
