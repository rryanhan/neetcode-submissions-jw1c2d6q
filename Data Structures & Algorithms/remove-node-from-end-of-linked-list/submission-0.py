# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
     
# n = 3  
# DUMMY    1      2       3       4      5       6       7       8
# s      
#                         f
# n = 3  
# DUMMY    1      2       3       4      5       6       7       8
#                                        s      
#                                                                f

# 1      2       3       4      5       6       7
#        s               f       

# 1      2       3       4      5       6       7
#                s                              f
# 
# 1      2       3       4      5       6       7
#                        s                              f
# here, need to skip fast.next(*n) and see if fast.next exists
# the node after slow is the one we need to change
# slow.next = slow.next.next
#
#