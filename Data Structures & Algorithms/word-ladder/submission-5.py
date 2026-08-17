class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        code = defaultdict(list)
        visited = set()

        time = 1

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                code[pattern].append(word)

        q = deque()
        q.append(beginWord)
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return time
                if word in visited:
                    continue
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighbourWord in code[pattern]:
                        q.append(neighbourWord)
                visited.add(word)
            time += 1
        return 0 
                

        
        