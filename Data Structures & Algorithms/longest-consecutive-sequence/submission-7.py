class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums.sort()
        if not nums:
            return 0
        current, streak = nums[0], 0
        i = 0
        # [1, 2, 2, 3]
        while i < len(nums):
            if current != nums[i]:
                streak = 0
                current = nums[i]
            while (i < len(nums)) and current == nums[i]:
                i += 1
                
            streak += 1
            current += 1
            longest = max(streak, longest)
        return longest
#.  [3, 4, 5, 10]
#. what do we need to keep track of?
#.    - current streak
#.    - longest streak
#.    - tracker of how far to go


#. 
# - what if there are duplicates?
# case 1 duplicate:
    # if current number == next number, move on, dont move current streak, update how far to go
# case 2 streak ends
    # update longest streak, keep tracker of how far to go at the next number, rest the streak 
# case 3 streak keeps going
    # update current streak, update tracker of how far to go
# - how do we reset the streak

# terminate once the index goes beyond the length

        
        

#   [2, 20, 4, 10, 3, 4, 5]
#
#   [2, 3, 4, 4, 5, 10, 20]
#    i
#
#
#
#
#


        