class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, n in enumerate(nums):
            diff = target - n

            # see if it exists
            if diff in res:
                return[res[diff], i]

            # if not, add to res
            res[n] = i



        