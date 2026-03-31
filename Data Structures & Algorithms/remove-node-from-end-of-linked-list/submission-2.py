# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeToRemove = head
        
        while n != 0:
            nodeToRemove = nodeToRemove.next
            n -= 1

        prev = None
        curr = head

        while nodeToRemove:
            nodeToRemove = nodeToRemove.next
            prev = curr
            curr = curr.next
        if prev is None:
            return head.next
        else:
            temp = curr.next
            curr.next = None
            prev.next = temp
        return head


