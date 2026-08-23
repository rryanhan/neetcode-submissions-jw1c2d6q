class Solution:
    def robber(self, nums):
            oneAhead, twoAhead = 0, 0
            
            for i in range(len(nums) -1, -1, -1):
                current = max(nums[i] + twoAhead, oneAhead)
                twoAhead = oneAhead
                oneAhead = current
            return oneAhead
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return nums[0]
        return max(self.robber(nums[1:]), self.robber(nums[:-1]))
        