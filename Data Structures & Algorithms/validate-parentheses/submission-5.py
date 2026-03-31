class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pDict = { ')' : '(', ']' : '[', '}' : '{'}

        for p in s:
            if p in pDict:
                if stack and stack[-1] == pDict[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        if not stack:
            return True
        else:
            return False



# ( [ { } ] )
# stack ->  ( 
# stack ->  ( [ 
# stack ->  ( [ {
# stack -> 
# add if not closing, if it is see if stack[-1] is matching pair
#
#
#
#