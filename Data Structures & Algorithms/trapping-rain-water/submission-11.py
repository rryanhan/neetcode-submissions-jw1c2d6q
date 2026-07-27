class Solution:
    def trap(self, height: List[int]) -> int:


        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                
                l += 1
                if leftMax - height[l] > 0:
                    res += min(leftMax, rightMax) - height[l]
                leftMax = max(height[l], leftMax)
            else:
                
                r -= 1
                if rightMax - height[r] > 0:
                    res += min(leftMax, rightMax) - height[r]
                rightMax = max(height[r], rightMax)
        return res

# if left is smaller than right:
    # update leftMax
    # move left forward
    # calculate height






# we can two pass this have have two arrays:
    # 1. 
        # leftMax, track for at current i, what highest is up to this point
        # rightMax
    
# or, we two pointer it with O(1) space and do it as we move pointers inwards

        