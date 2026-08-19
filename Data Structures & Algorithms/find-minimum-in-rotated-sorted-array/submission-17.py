class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if l == r:
                return nums[mid]
            if nums[mid] < nums[r]: # right side sorted
                # check left side
                r = mid
            else: # mid greater than nums[r], def not the minimum
                l = mid + 1

        return mid
# 0 1
# 1 0

# 1 2 3 4 5

# 2 3 4 1
