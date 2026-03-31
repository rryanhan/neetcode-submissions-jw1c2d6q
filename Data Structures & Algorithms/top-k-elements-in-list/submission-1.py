class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        le = len(nums)
        kms = [[] for i in range(le + 1)]

        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for number, frequency in count.items():
            kms[frequency].append(number)
        
        result = []
        for i in range(len(kms)-1, -1, -1):
            for val in kms[i]:
                result.append(val)
                if len(result) == k:
                    return result


        
        