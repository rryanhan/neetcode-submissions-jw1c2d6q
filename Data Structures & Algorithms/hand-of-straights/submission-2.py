class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False
        dic = Counter(hand)
        minHeap = list(dic.keys())
        heapq.heapify(minHeap)

        # minHeap keeps track of minimum values
        while minHeap:
            minVal = minHeap[0]

            for i in range(minVal, minVal + groupSize):
                # if no more occurrences left, false
                if dic[i] == 0:
                    return False

                # decrement count by 1
                dic[i] -= 1

                if dic[i] == 0:
                    heapq.heappop(minHeap)

        return True
        


# greedy:
# choose the smallest value we can that is available to start the streak

# dic to keep track of occurrences per value
#[1, 2, 3, 4, 5, 6] size = 3
# [1, 2, 3] THEN [4, 5, 6]