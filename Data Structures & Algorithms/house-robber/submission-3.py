class Solution:
    def rob(self, nums: List[int]) -> int:
        take = 0
        skip = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            temp = max(skip, nums[i] + take)
            take, skip = skip, temp

        return skip