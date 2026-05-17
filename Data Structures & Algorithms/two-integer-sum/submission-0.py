class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lw = 0
        hi = len(nums) - 1

        while lw < hi:
            if nums[lw] + nums[hi] == target:
                return [lw, hi]
            hi -= 1
            if lw == hi:
                lw += 1
                hi = len(nums) -1
        
        