class Solution:
    def rob(self, nums: List[int]) -> int:
        value = [0] * len(nums)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        value[0] = nums[0]
        value[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            value[i] = max(value[i-1], nums[i] + value[i-2])
        return value[len(nums)-1]