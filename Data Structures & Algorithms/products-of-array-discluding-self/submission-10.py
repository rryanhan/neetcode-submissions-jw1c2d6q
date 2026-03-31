class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        final = [1] * len(nums)

        for i in range(len(nums)):
            final[i] = pre
            pre *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            final[i] *= post
            post *= nums[i]
        return final

# pre   1,  1,  2,  8
# post  8,  24, 6,  1
# final 48, 24, 12, 8
        