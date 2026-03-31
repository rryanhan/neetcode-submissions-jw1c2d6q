class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")" : "(" , "}" : "{" , "]" : "["}

        for ch in s:
            if ch in dic:
                if stack and stack[-1] == dic[ch]:
                    stack.pop()
                else: return False
            else:
                stack.append(ch) 

        if not stack:
            return True
        else: 
            return False       



# the solution is the hasmap
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