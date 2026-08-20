class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()
        # build list
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                print(word1[:len(word2)], word2)
                return "" 
            c = 0

            while c < min(len(word1), len(word2)):
                if word1[c] != word2[c]:
                    adj[word1[c]].add(word2[c])
                    break
                c += 1    



        visited = set()
        visiting = set()
        res = []
        def dfs(char):
            
            if char in visited:
                return True
            if char in visiting:
                return False
            visiting.add(char)
            for laterChar in adj[char]:
                if not dfs(laterChar):
                    return False
            visiting.remove(char)
            visited.add(char)
            res.append(char)
            return True
        
        for c in adj:
            if not dfs(c):
                print(c)
                return ""
        res.reverse()
        return "".join(res)










