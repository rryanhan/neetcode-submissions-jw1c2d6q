class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finlist = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            finlist[i] = prefix
            prefix *= nums[i]
        postfix = 1

        for j in range(len(nums) -1, -1, -1):
            finlist[j] *= postfix
            postfix *= nums[j]
        return finlist