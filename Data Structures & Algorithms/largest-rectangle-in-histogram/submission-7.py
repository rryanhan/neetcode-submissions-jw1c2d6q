class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            # pop from stack
            # if current height is shorter than what we pop from, 
            # it can start extending from there
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start = index
            stack.append([start, h])
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        
        return res

        
# a rectangle can keep extending right until it hits a shorter bar

# we want a stack to keep track of indices that can still run along 
# the length of heights
    # this means the height in the stack needs to be greater than
    # the index we are at

# stack contains: [height, index_its_at]
