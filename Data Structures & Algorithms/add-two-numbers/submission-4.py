# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        curr = new
        carryon = 0

        while l1 or l2 or carryon:
            if l1:
                l1val = l1.val
            else: 
                l1val = 0
            if l2:
                l2val = l2.val
            else: 
                l2val = 0
            
            summation = l1val + l2val + carryon
            curr.next = ListNode(summation%10)
            carryon = summation//10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
            
        return new.next

        


#
#
# 9
# 9
# carry variable becomes 1
# l1(one's place of 9+9 which is 8) -> Node(carryvariable)
#
# DUMMY -> 8 1
# 9 9 9 
# 9 9 9
#carryon = 1
#DUMMY -> 8 9 9 1
# 1998
# 8991
# 9 9 9 9 9
# 9 9 9

# 8 9 9 0 0 1
# 100998
# 899001
# if we are at the end, prev->next = 1