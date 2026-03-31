class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        result = []
        while r < len(s):
            while s[r] != "#":
                r += 1
            length = int(s[l : r])
            string = s[r + 1: length + r + 1]
            result.append(string)
            l = r + length + 1
            r = l
        return result

        
        
#.   4#need4#code4#love3#you
       






# [ "neet","code","love","you" ]
# 4*need4*code4*love3*you
# ^                         l
#  ^                        r
# while s[l] != '*', r += 1
# length = int(s[l:r])
# append.(s[r:length + r + 1])
# l = r