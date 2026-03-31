class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for number, freq in count.items():
            bucket[freq].append(number)
        res = []
        for i in range(len(bucket) -1, -1, -1):
            for number in bucket[i]:
                res.append(number)
                if len(res) == k:
                    return res
        return res

        
        
# bucket keeps track of occurences : number