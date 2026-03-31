# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        prev, curr = None, second
        while curr:
            dummy = curr.next
            curr.next = prev
            prev = curr
            curr = dummy

        first, second = head, prev
        while second:
            firstTemp, secondTemp = first.next, second.next
            first.next = second
            second.next = firstTemp
            first, second = firstTemp, secondTemp

# 2   4   6   8   10
# s   f

# 2   4   6   8   10
#     s       f

# 2   4   6   8   10
#         s           f



