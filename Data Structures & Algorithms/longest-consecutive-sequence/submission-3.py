class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        maximum = 0
        i = 0
        curr = nums[0]
        streak = 0
        while i < len(nums):
            if curr != nums[i]:
                streak = 0
                curr = nums[i]
            while i < len(nums) and curr == nums[i]:
                i += 1
            curr += 1
            streak += 1
            maximum = max(streak, maximum)

        return maximum


#   [2, 20, 4, 10, 3, 4, 5]
#
#   [2, 3, 4, 4, 5, 10, 20]
#    i
#
#
#
#
#


        