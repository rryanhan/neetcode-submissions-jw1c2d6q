class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = defaultdict(int)
        for char in t:
            tCount[char] += 1

        NEED = len(tCount)
        HAVE = 0

        l, r = 0, 0
        sCount = defaultdict(int)
        res = ""
        resLen = 99999


        while r < len(s):
            char = s[r]
            # 1. update sCount
            sCount[char] += 1
            if sCount[char] == tCount[char]:
                HAVE += 1

            # 2. check HAVE == NEED
                # update res

                
            
            # 3. shrink window if we need
            
            while HAVE == NEED:
                if resLen > (r - l + 1):
                    resLen = r - l + 1
                    res = s[l : r + 1]
                leftChar = s[l]
                sCount[leftChar] -= 1
                if sCount[leftChar] < tCount[leftChar]:
                    HAVE -= 1
                l += 1
            r += 1
        return res if resLen != 99999 else ""


        


# HAVE, and NEED
    # have is # of unique character counts
# also need a dictionary count as we traverse, charCount{}

# NEED is for each character, how many we need

# 1. set up the NEED

# 2. update HAVE as we traverse the window
    # r += 1, update using r

# 3. if HAVE == NEED:
    # update res
    # start shrinking the window
