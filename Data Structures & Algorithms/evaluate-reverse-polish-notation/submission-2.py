class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sol = []
        for c in tokens:
            if c == "+":
                a = int(sol.pop())
                b = int(sol.pop())
                sol.append(a+b)
            elif c == "*":
                a = int(sol.pop())
                b = int(sol.pop())
                sol.append(a*b)
            elif c == "-":
                a = int(sol.pop())
                b = int(sol.pop())
                sol.append(b-a)
            elif c == "/":
                a = int(sol.pop())
                b = int(sol.pop())
                sol.append(int(b/a))
            else:
                sol.append(int(c))
        return sol[0]


        