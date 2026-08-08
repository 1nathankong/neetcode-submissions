class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p={}
        for i,a in enumerate(nums):
            check = target - a
            if check in p:
                return [p[check], i]
            p[a] = i