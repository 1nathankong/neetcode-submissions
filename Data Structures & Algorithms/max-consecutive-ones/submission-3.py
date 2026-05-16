class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                if current > max_count:
                    max_count = current
            else:
                current = 0
        return max_count
        