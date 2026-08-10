class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high = 0, len(nums)-1
        
        while low <= high:
            mid = (low + high) // 2
            print("low value:", nums[low])
            print("mid value:",nums[mid])
            print("high value:", nums[high])
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[mid]