class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            newString = ''.join(sorted(s))
            result[newString].append(s)
        return result.values()


# for each string in list, sort using ''.join 
# use that as the key
# if it exists (default dict manages), append on that key
#
#

        