class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        A = len(set(nums))
        B = len(nums)
        return A < B
        