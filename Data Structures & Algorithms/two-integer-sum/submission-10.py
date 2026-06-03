class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in dic:
                return [dic[difference], i]
            dic[n] = i

# 7 - 3 = 4

# put 3 in with its index {number : index}

# 7 - 4 = 3

# return [dic[4], index]
        