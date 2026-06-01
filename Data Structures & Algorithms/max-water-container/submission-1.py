class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0

        while left < right:
            area = max(area, min(heights[left], heights[right]) * (right - left))
            left += 1

            if left == right:
                left = 0
                right -= 1
        return area
