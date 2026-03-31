class Solution:
    def rob(self, nums: List[int]) -> int:
        next2 = 0
        next1 = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            temp = max(next1, nums[i] + next2)
            next1, next2 = temp, next1

        return next1