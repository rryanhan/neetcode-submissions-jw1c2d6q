class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        for char in t:
            countT[char] += 1
        
        have, need = 0, len(countT)
        l = 0
        window = defaultdict(int)
        res = ""
        resLen = 99999
        for r in range(len(s)):
            window[s[r]] += 1

            if window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if resLen > (r - l + 1):
                    res = s[l : r + 1]
                    resLen = (r - l + 1)
                
                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return res




        

# 1. count the number of unique elements in t -> need
    # also count frequency for each element

# 2. traverse through s with l and r pointers
    # everytime charCount matches, have += 1

    # only shrink when have == need
        # update the output string
        # remove unique character count as l moves inward

# have, need = int
# window, countT = {}, {}