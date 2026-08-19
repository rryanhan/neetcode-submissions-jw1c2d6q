class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = ""
        res = ""
        stack = []

        for c in path + "/":
            if c == "/":
                if curr == "" or curr == ".":
                    curr = ""
                    continue
                if curr == "..":
                    if stack:
                        stack.pop()
                else: 
                    stack.append(curr)
                curr = ""
            else:
                curr += c
        return "/" + "/".join(stack)




# slashes you need to evaluate the current string we have:
    # .. means you pop back 
    # . means you do nothing
    # anything else means we add it to the stack, provided we have built a string
        