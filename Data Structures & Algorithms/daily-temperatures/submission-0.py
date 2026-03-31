class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]* n
        for t in range(n):
            count = 0
            pointer = t
            while pointer < n:
                if temperatures[t] < temperatures[pointer]:
                    result[t] = count
                    break
                else:
                    count +=1
                    pointer +=1
           
        return result

        