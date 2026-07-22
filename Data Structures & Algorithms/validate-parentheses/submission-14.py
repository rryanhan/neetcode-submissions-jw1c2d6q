class Solution:
    def isValid(self, s: str) -> bool:
        p = {"]" : "[", ")" : "(", "}" : "{"}
        stack = []
        for paren in s:
            if stack and paren in p:
                if stack[-1] == p[paren]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(paren)
        return True if not stack else False




#( [ { } ] )
# if it isnt a closing stack, append
# if it is, check to see if it matches the dic value of the top of the stack
# if so, pop the stack
# return if stack is empty