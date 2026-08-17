class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quad = []
        res = []
        nums.sort()

        def kSum(k, index, target):
            # as long as k != 2:
                # find a unique value
                # add it to quad
                # recurse, updating k, index we are and target
                # pop quad

            # run 2sum II
            if k != 2:
                for i in range(index, len(nums)):
                    if i > index and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            
            l, r = index, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            
        kSum(4, 0, target)
        return res

        