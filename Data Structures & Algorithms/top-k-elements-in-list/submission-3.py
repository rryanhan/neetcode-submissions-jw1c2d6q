class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        s = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for key, value in freq.items():
            s.append([value, key])

        s.sort()

        finalList = []
        while len(finalList) < k:
            finalList.append(s.pop()[1])
        return finalList







# 1      2       2       3       3       3
#
# dictionary{1 : 1, 2 : 2, 3 : 3}
#
# [ [1, 2]  [2, 2]  [3, 3]]
#
# 
#
#
#

        