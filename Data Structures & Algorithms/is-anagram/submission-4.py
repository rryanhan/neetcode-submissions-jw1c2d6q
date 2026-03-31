class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        Sset, Tset = {}, {}

        for i in range(len(s)):
            Sset[s[i]] = Sset.get(s[i], 0) + 1
            Tset[t[i]] = Tset.get(t[i], 0) + 1
        return Sset == Tset


        
# if s.length != t.length: return False

# Sset, Tset = {}, {}
# 
# for each index in Sset (range(len(s)))
# create key value pair, key being letter, value occurences
# 
# see if the two sets are equal to each other
# s = "racecar", t = "carrace" length 7, 0-6
#
#

