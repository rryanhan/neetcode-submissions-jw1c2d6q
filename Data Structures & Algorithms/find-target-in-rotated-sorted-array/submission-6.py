class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r ) // 2
            if nums[mid] == target:
                return mid

            # determine which side of the array is sorted
            if nums[l] <= nums[mid]: #[ 3, 4, 5, 6, 1, 2]
                # means the left side is sorted
                # is the target inside the left side?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                    # target is on the right side
                else:
                    l = mid + 1
            
            # right side is sorted
            else:
                # is the target inside the right side?
                if nums[r] >= target > nums[mid]: 
                    l = mid + 1
                    # target is on the left side
                else:
                    r = mid - 1

        return -1

# the things we need to check: 
# - which side of the array is sorted, 
#   and is the target in the sorted array?

# [3, 4, 5, 6, 1, 2], target = 1
# - here, the left side is sorted, because l <= mid
# - however, the target is outside of the array, because 
#.  target > mid

# [6, 1, 2]
# - here, the right side is sorted, because l > mid
# - and, the target is inside the right side, because
#   target > mid



        
