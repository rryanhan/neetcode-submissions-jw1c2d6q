class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -9999
        localMax = 0


        for n in nums:
            localMax += n
            res = max(res, localMax)
            if localMax < 0:
                localMax = 0
        return res

        


# at each stop:
# do i extend the subarray, or reset it?

# this will depend on the sum of the subarray
# if it goes in the negatives, we reset it
# - negatives are a liability