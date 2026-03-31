class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []
        result = []
        preM = 1
        for i in range(len(nums)):
            pre.append(preM)
            preM *= nums[i]
        postM = 1
        for i in range(len(nums) -1, -1, -1):
            post.append(postM)
            postM *= nums[i]
        postFinal = post[::-1]
        for i in range(len(nums)):
            result.append(pre[i] * postFinal[i])
        return result



# [ 1 2 3 4 ]
# [ 1 2 6 24]  -> pre
# [24 24 12 4] -> post
        