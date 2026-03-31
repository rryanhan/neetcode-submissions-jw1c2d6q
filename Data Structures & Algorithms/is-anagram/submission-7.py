class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for i in range(len(s)):
            if countS[s[i]] != countT.get(s[i], 0):
                return False
        return True
        


        
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

