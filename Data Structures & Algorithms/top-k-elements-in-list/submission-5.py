class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        maxHeap = []
        for number, freq in count.items():
            heapq.heappush(maxHeap, (-freq, number))
        res = []
        while len(res) != k:
            freq, number = heapq.heappop(maxHeap)
            res.append(number)
        return res
        