class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxH = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxH = max(maxH, area)
            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
        return maxH
        


# min (height l and height r) * difference in the 2
# if heights[l] > heights[r]
#   - we can move r down 1 and vice versa
# we just want to maximize for the heights, so we can 
# adjust pointers based on that