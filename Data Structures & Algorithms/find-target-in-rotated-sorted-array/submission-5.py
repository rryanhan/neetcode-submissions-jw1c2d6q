class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r ) // 2
            if nums[mid] == target:
                return mid

            # which half is sorted?
            if nums[l] <= nums[mid]:
                # left half is sorted.
                # if target is NOT in [nums[l], nums[mid]], search right half
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # otherwise target is in the left half
                else:
                    r = mid - 1
            else:
                # right half is sorted.
                # if target is NOT in [nums[mid], nums[r]], search left half
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

        
