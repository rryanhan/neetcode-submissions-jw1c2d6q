class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max (length, longest)

        return longest
        

#   [2, 20, 4, 10, 3, 4, 5]
#
#   [2, 3, 4, 4, 5, 10, 20]
#    i
#
#
#
#
#


        