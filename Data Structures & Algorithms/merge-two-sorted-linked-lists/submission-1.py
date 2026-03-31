# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy1, dummy1next = list1, list1.next
        dummy2, dummy2next = list2, list2.next
        if dummy1.val <= dummy2.val:
            dummy1.next = self.mergeTwoLists(dummy1next, dummy2)
            return dummy1
        else:
            dummy2.next = self.mergeTwoLists(dummy1, dummy2next)
            return dummy2

# 1    2    4
#
# 1    3    5
#
#
            

#  1 -> 2 -> 4      1 -> 3 -> 5
# if list 1 and list 2 head are null, return new list
#  if list 1 doesnt exist but list 2 does, add head of list 2
# if list 2 doesnt exist but list 1 does, add head of list 1
# if both exist, see which head value is greater; add the greater one and mve
#
#

        