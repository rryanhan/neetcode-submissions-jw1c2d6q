# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev  
# [1, 2, 3, 4, 5, 6]
#  p  c  t
# curr = 2->1
# temp = 3->4->5->6


# start with curr, prev = null
# as long as curr exists, set curr to prev
# move prev to curr, and curr to next
#
#
#


        