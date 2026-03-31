class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]: # left side is sorted
                if nums[l] <= target < nums[mid]: 
                    r = mid - 1 # nums in left
                else: 
                    l = mid + 1
            else: # right side is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1 # nums in right
                else: 
                    r = mid - 1
        return -1

        







# [3, 4, 5, 6, 1, 2] target = 1
#        m
# - is left less than target?
# - is target less than mid?
# left is less than mid, but mid is greater than target. 
# that means it is on the right side

#[3, 4, 5, 6, 1, 2] target = 6
# left is less than mid, but mid is less than target
# that means target is on the right side

#[5, 6, 7, 1, 2, 3, 4] target = 5
# left is greater than mid, and mid is less than target
# means it is on the left side

#[7, 1, 2, 3, 4, 5, 6] target = 1
# left is greater than mid, and mid is greater than target
# means it is on the left side
















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



        
