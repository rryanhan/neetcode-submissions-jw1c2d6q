# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        
        if not list1:
            head.next = list2
        else: 
            head.next = list1
        return dummy.next


# if not list 1, add rest of list 2
# if not list 2, add rest of list 1

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

        