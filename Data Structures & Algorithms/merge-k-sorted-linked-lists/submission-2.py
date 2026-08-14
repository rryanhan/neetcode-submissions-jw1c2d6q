# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        # merge helper
        def mergeHelper(l1, l2):
            dummy = ListNode(0)
            curr = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next  = l1
                    curr = curr.next
                    l1 = l1.next
                else:
                    curr.next  = l2
                    curr = curr.next
                    l2 = l2.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return dummy.next
        
        while len(lists) != 1:
            dummyList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                merged = mergeHelper(l1, l2)
                dummyList.append(merged)
            lists = dummyList
        return lists[0]



        
        # while len(lists) != 1
        # get lists, merge lists[i] with lists[i + 1]
            # if there is odd number, merge lists[i] with empty list
        # keep track of dummy list, replace lists with dummy list after for loop

        

# merge sort
# OR min heap