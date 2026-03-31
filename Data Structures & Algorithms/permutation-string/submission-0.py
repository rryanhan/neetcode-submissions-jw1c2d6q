class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1 = sorted(s1)
        string1 = "".join(set1)

        string2 = ""

        l = 0

        for r in range(len(s2)):
            while r-l+1 > len(string1):
                l += 1
            if "".join(sorted(s2[l:r+1])) == string1:
                return True
        return False
        