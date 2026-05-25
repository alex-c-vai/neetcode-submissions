class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        # find the pivot
        # 11 1 3 5 7 9.   t = 11
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        pivot = l
        l, r = 0, len(nums)-1
        if nums[pivot] <= target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1