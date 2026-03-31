class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            num = len(s)
            res += str(num) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:
        result = []
        r = 0
        while r != len(s):
            l = r
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            l = r + 1
            r = l + length
            result.append(s[l:r])
        return result


# [ "neet","code","love","you" ]
# 4*need4*code4*love3*you
# ^                         l
#  ^                        r
# while s[l] != '*', r += 1
# length = int(s[l:r])
# append.(s[r:length + r + 1])
# l = r