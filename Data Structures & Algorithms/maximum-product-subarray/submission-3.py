class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        smallest, largest = 1, 1

        
        for n in nums:
            prev_smallest, prev_largest = smallest, largest
            largest = max(prev_smallest * n, prev_largest * n, n)
            smallest = min(prev_smallest * n, prev_largest * n, n)

            res = max(res, largest)


        return res

# the smallest product can become the largest product, vice versa
    # keep track of the largest product we've seen, and the smallest