class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for l in range(len(nums)-2):
            if l != 0 and nums[l] == nums[l - 1]:
                continue
            r = len(nums) - 1
            m = l + 1
            while m < r:
                if nums[l] + nums[m] + nums[r] < 0:
                    m += 1
                    
                elif nums[l] + nums[m] + nums[r] > 0:
                    r -=1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -=1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1

        return res



# -2 -2 -2 0 0 0 1 2 3 4 4