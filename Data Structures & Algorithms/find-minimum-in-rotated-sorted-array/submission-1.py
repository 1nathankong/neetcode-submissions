class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        min = nums[0]

        for i in range(n):
            if min > nums[i]:
                min = nums[i]
        return(min)
        