class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        # {a : set(b)}
            # this means that a comes EARLIER than b
        for word in words:
            for c in word:
                adj[c] = set()
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            # check if lexicographically comprehensive
                # if word1 is larger than word2, and word2 is a prefix
            
            if len(word1) > len(word2) and word1[:len(word2)] == word2[:len(word2)]:
                return ""
            
            # find first different character
            m = 0
            while m < min(len(word1), len(word2)):
                if word1[m] != word2[m]:
                    adj[word1[m]].add(word2[m])
                    break
                else:
                    m += 1
        
        visiting = set()
        visited = set()
        res = []

        def dfs(char):
            # if we're looping back to a character we've already seen, False
                # means contradiction in which word comes earlier
            if char in visiting:
                return False
            if char in visited:
                return True
            
            visiting.add(char)

            for laterChars in adj[char]:
                if not dfs(laterChars):
                    return False
            visiting.remove(char)
            visited.add(char)
            res.append(char)
            return True
            


        for character in adj:
            if not dfs(character):
                return ""
        res.reverse()
        return "".join(res)

                









# build an adjacency list

        