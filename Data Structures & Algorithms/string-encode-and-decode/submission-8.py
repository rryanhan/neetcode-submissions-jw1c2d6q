class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0

        while r < len(s):
            while s[r] != "#":
                r += 1
            length = int(s[l : r])
            res.append(s[r + 1 : r + 1 + length])
            l = r + 1 + length
            r = l
        return res




# we can have <number># 

# this gives us the length of the string, and once we hit the pound, we can
# extract the length of the string and update the pointers

# 5#Hello5#World