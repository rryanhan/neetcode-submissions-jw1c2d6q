class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            solution = numbers[l] + numbers[r]
            if target > solution:
                l +=1
            if target < solution:
                r -=1
            if target == solution:
                return [l+1, r+1]




# 1      2       3       4
# l                      r
#
# if target is greater than solution
#
#
#
#
