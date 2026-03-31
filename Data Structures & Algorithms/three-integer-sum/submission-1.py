class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if left < right and nums[left] + nums[right] + nums[i] > 0:
                    right -=1
                elif left < right and nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    res.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

            
        return res

  
        

            
        
        