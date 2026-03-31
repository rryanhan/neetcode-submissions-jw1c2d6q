class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            res[tuple(key)].append(s)
        return list(res.values())
        



# for each string in list, sort using ''.join 
# use that as the key
# if it exists (default dict manages), append on that key
#
#

        