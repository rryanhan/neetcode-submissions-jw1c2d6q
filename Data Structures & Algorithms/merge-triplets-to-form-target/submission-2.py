class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False] * 3
        prune = []
        for first, second, third in triplets:
            if first > target[0] or second > target[1] or third > target[2]:
                continue

            if first == target[0]:
                res[0] = True
            if second == target[1]:
                res[1] = True
            if third == target[2]:
                res[2] = True
        return all(res)
        

# if there is ever a case where val at index > target[i], prune out

# if a val is equal to target, add to solution