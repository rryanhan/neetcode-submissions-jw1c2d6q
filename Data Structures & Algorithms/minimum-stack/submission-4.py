class MinStack:

    def __init__(self):
        # normal stack
        self.stack = []

        # keeps order highest to lowest
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack == []:
            smallest = val
        else:
            smallest = min(val, self.minStack[-1])
        self.minStack.append(smallest)

        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
# push 1
# - minStack return 1
# [ 1 ]

# push 2
# minStack return 1
# [ 1, 1]

# push 0
# minStack return 0
# [ 1, 1, 0]