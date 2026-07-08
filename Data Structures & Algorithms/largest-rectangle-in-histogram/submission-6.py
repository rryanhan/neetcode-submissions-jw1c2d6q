class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            # check if we need to pop stack
            while stack and stack[-1][1] > h:
                # pop
                index, height = stack.pop()
                #check for max area
                res = max(res, height * (i - index))
                
                # update earliest index we can start from
                start = index

            stack.append((start, h))
        
        # finish computing the bars that extend all the way
        for i, h in stack:
            res = max(res, (h * (len(heights) - i)))
        
        return res