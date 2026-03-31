class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        result = 0


        for n in nums:
            streak = 1
            if (n-1) not in numset:
                while (n + streak) in numset:
                    streak += 1
            result = max(result, streak)
        return result

#.  [3, 4, 5, 10]
#. what do we need to keep track of?
#.    - current streak
#.    - longest streak
#. 
# - what if there are duplicate?
# - how do we reset the streak

        
        

#   [2, 20, 4, 10, 3, 4, 5]
#
#   [2, 3, 4, 4, 5, 10, 20]
#    i
#
#
#
#
#


        