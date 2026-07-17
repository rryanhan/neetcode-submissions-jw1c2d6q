# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, curr = groupNext, groupPrev.next
            # so it points to the next node in the group

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            tmp = groupPrev.next # save the old start of the group
            groupPrev.next = kth # putting kth at beginning
            groupPrev = tmp # the old start of the group becomes the node before the next reversal

        return dummy.next




    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# dummy -> 1 -> 2 -> 3 -> 4 -> 5 ->
# dummy -> 
