class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                if pattern not in adj: adj[pattern] = []
                adj[pattern].append(word)
        

        q = collections.deque([beginWord])
        visit = set([beginWord])
        dist = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return dist
                
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in adj.get(pattern, []):
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)

            dist += 1

        return 0
