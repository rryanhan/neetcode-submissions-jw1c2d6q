class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixWord = strs[0]
        res = ""

        for i in range(len(prefixWord)):
            for word in strs[1:]:
                if i >= len(word) or prefixWord[i] != word[i]:
                    return res
            res += prefixWord[i]
        return res
        