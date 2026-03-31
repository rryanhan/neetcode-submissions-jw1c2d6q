class Solution:
    def maxArea(self, heights: List[int]) -> int:
       
        maximum = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            volume = min(heights[l], heights[r]) * (r-l)
            maximum = max(maximum, volume)
            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
        return maximum