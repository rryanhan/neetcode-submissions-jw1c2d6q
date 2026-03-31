class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalVal = 0
        start = 0
        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            totalVal += diff
            if totalVal < 0:
                start = i + 1
                totalVal = 0
        return start if totalVal >= 0 else -1

        


# total(gas) HAS to be >= than total(cost)

# gas(i) - total(i)
# - if it ever goes negagive, reset to 0
# - if by end of for loop it is >=0, loop works
# - if so, return the earliest index we did not have to reset