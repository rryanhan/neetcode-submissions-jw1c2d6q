class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 1, x
        res = -9999

        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if mid * mid == x:
                return mid
            if mid * mid > x:
                # need to search lower
                r = mid - 1
            else:
                # put as valid, look for larger numbers
                res = max(res, mid)
                l = mid + 1
        return res

# 1  2  3  4  5  6  7  8  9
#             m 

        