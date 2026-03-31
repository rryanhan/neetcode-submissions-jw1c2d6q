class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            string = s[j + 1 : j + 1 + length]
            res.append(string)
            i = j + 1 + length
        return res
#.   4#need4#code4#love3#you


# [ "neet","code","love","you" ]
# 4*need4*code4*love3*you
# ^                         l
#  ^                        r
# while s[l] != '*', r += 1
# length = int(s[l:r])
# append.(s[r:length + r + 1])
# l = r