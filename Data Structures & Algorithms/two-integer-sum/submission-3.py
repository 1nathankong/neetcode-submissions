class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = 0
        b = len(nums) - 1

        while a<b:
            if nums[a] + nums[b] == target:
                return [a,b]
            b -= 1
            if a == b:
                a += 1
                b = len(nums) - 1
        