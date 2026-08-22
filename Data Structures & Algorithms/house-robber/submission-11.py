class Solution:
    def rob(self, nums: List[int]) -> int:
        oneAhead, twoAhead = 0, 0
        
        for i in range(len(nums) -1, -1, -1):
            current = max(oneAhead, nums[i] + twoAhead)
            twoAhead = oneAhead
            oneAhead = current
        return oneAhead
        
        