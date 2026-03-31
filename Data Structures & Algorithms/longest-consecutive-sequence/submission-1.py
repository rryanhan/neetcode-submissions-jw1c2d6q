class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        longest = 0

        for n in numsset:
            currentNum = n
            streak = 0
            while currentNum in numsset:
                currentNum += 1
                streak +=1
            longest = max(streak, longest)
        return longest