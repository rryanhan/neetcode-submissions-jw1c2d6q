class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = [0] * len(height), [0] * len(height)

        # process leftMax
        leftPointer = 0
        for i in range(len(height)):
            leftMax[i] = leftPointer
            leftPointer = max(leftPointer, height[i])


        #process rightMax
        rightPointer = 0
        for i in range(len(height) - 1, -1, -1):
            rightMax[i] = rightPointer
            rightPointer = max(rightPointer, height[i])

        
        res = 0
        # find rainwater
        for i, h in enumerate(height):
            bar = min(leftMax[i], rightMax[i])
            if bar - h > 0:
                res += bar - h

        return res



# we can two pass this have have two arrays:
    # 1. 
        # leftMax, track for at current i, what highest is up to this point
        # rightMax
    
# or, we two pointer it with O(1) space and do it as we move pointers inwards

        