class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        counter = 0
        max_count = 0
        for i in range(n):
            if nums[i] == 1:
                counter += 1
                max_count = max(max_count, counter)
            else:
                counter = 0 
            
        return max_count
        