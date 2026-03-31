class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        countArray = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        for number, frequency in freq.items():
            countArray[frequency].append(number)
        res = []
        for i in range(len(countArray) -1, 0, -1):
            for n in countArray[i]:
                res.append(n)
                if len(res) == k:
                    return res
        