class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 0

        for i in range(n-1, -1, -1):
            cur = one + two
            temp = one
            one = cur
            two = temp
        return one
        
# n = 5
# 0, 1, 2, 3, 4, 5

#      5,  4,  3,  2,  1,  0
#. two one i