class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        A = len(set(nums))
        B = len(nums)
        if A == B: return False 
        else: return True
        