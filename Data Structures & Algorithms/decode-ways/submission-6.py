class Solution:
    def numDecodings(self, s: str) -> int:
        singleDig = 1
        doubleDig = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                temp = 0
            elif ((i + 1) < len(s)) and ((s[i] == "1") or (s[i] == "2" and s[i+1] in "0123456")): 
                temp = singleDig + doubleDig
            else:
                temp = singleDig
            singleDig, doubleDig = temp, singleDig
                
        return singleDig

        #1 2 3 
        # 1 2 3
        # 12 3
        # 1 23