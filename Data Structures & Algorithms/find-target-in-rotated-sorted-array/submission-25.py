class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)// 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        



# mid > l
#   

# if mid is greater than l, left side is sorted
#    so now we see if target is in this bound
#       if it is, search left


# if mid is less than l, right side is sorted

# [6, 1, 2, 3, 4, 5]