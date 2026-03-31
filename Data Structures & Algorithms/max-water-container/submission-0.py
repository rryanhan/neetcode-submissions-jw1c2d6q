class Solution:
    def maxArea(self, heights: List[int]) -> int:
       
        maximum = 0
        n = len(heights)

        for i in range(0, n - 1):
            for j in range(i+1, n):
                length = j - i
                volume = min(heights[i], heights[j]) * length
                maximum = max(volume, maximum)
        return maximum