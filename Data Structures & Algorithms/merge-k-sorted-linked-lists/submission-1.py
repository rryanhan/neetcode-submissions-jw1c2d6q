# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i, ll in enumerate(lists):
            if not ll:
                continue
            heapq.heappush(minHeap, (ll.val, i, ll))
            print(minHeap)
        
        res = ListNode(0)
        dummy = res

        while minHeap:
            value, index, ll = heapq.heappop(minHeap)
            dummy.next = ll
            dummy = dummy.next

            if not ll.next:
                continue
            heapq.heappush(minHeap, (ll.next.val, index, ll.next))
        
        return res.next

        # step 1:
        # add the lists into the minHeap

        # step 2:
        # keep going while the minHeap exists
            # - if the node exists (not null), append it to res and move it to next node

        
        



# two ways to solve:
    # 1: merge two lists at a time, then merge those into each other

    # 2: minHeap the linkedlists so we are merging the smallest value every time

