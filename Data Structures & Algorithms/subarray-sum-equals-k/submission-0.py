class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixDic = defaultdict(int)
        prefixDic[0] += 1
        res = 0
        runningSum = 0

        for i, n in enumerate(nums):
            runningSum += n
            if runningSum - k in prefixDic:
                res += prefixDic[runningSum - k]
            prefixDic[runningSum] += 1
        return res


        



# running sum - prefix sum = k

# running sum - k = prefix sum

# 3  -1  1  2
#     <----->  2
# <----------> 5

# 3 : 1
# 2 : 1
# 3: 1
# 5 : 1


# k = 2
