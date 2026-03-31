class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasD = set()
        for n in nums:
            if n in hasD:
                return True
            hasD.add(n)
        return False
        