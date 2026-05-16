class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        counter = 0
        max_count = 0
        for i in range(n):
            if nums[i] == 1:
                print("adding 1")
                counter += 1
            else:
                print("resetting to 0")
                counter = 0 
            max_count = max(max_count, counter)
        return max_count
        