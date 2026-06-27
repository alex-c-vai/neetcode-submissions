class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax = 1, 1
        maxProd = nums[0]

        for num in nums:
            temp = currMax * num
            currMax = max(num*currMax, num*currMin, num)
            currMin = min(temp, num*currMin, num)
            maxProd = max(maxProd, currMax)
            
        return maxProd