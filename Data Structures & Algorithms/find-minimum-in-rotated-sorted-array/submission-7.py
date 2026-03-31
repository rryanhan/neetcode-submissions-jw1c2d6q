class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else: 
                l = mid + 1
        if l == r:
            return nums[l]
        


# [3,4,5,6,1,2]
# find the middle and recurse on the left or right side, 
# depending on if mid is larger or smaller than the rightmost element
# has to be <=