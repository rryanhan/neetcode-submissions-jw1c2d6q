class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        val = [0] * 26
        for i in range(len(t)):
            val[ord(s[i]) - ord('a')] += 1
            val[ord(t[i]) - ord('a')] -= 1
        for i in val:
            if i != 0:
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

