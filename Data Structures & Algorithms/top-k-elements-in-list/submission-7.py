class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kCounter = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for number, freq in kCounter.items():
            bucket[freq].append(number)
        res = []
        t = 0

        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                t += 1
                if t == k:
                    return res





# 
        