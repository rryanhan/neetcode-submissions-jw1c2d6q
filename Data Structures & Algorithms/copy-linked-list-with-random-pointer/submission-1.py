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
        nodeDict = {}
        curr = head
        while curr:
            nodeDict[curr] = Node(curr.val)
            curr = curr.next
        twohead = head
        dummy = twohead
        while twohead:
            dumNode = nodeDict.get(twohead)
            dumNode.next = nodeDict.get(twohead.next)
            dumNode.random = nodeDict.get(twohead.random)
            twohead = twohead.next
        return nodeDict.get(dummy)








# two pass dictionary 
# pass 1 -> dict[node] = just the val
# pass 2 -> newList
#
#
#
#
#
        