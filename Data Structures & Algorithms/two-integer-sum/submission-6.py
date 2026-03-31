class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        isSeen = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in isSeen:
                return [isSeen[val], i]
            isSeen[nums[i]] = i
       


   