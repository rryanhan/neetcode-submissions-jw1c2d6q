class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:
    
    def __init__(self):
        self.root = None
    
    def insert(self, startTime, endTime):
        curr = self.root
        while curr:
            #if completely before:
            if endTime <= curr.start:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(startTime, endTime)
                    return True

            # if completely after:
            elif startTime >= curr.end:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(startTime, endTime)
                    return True


            # else its false 
            else:
                return False

        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = TreeNode(startTime, endTime)
            return True
        return self.insert(startTime, endTime)
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
#   <--------->
# <---->.        <------>