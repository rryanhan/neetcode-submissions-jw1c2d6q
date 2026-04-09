"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {None : None}

        curr = head
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
        
        dummy = Node(0)
        start = dummy

        curr2 = head
        while curr2:
            deepCopy = dic[curr2]
            deepCopy.next = dic[curr2.next]
            deepCopy.random = dic[curr2.random]
            dummy.next = deepCopy
            dummy = dummy.next
            curr2 = curr2.next
        return start.next
        