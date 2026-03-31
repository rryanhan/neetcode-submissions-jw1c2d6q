class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        n = len(heights)
        for i in range(n):
            height = heights[i]
            rightM = i + 1
            while rightM < n and height <= heights[rightM]:
                rightM += 1
            leftM = i - 1
            while leftM >= 0 and height <= heights[leftM]:
                leftM -= 1
            leftM += 1
            rightM -= 1
            maxA = max(maxA, (height * (rightM-leftM +1)))
        return maxA
            
