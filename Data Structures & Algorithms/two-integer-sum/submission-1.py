class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p={}
        for i,a in enumerate(nums):
            if (target - a) in p:
                return [p[target - a], i]
            p[a] = i