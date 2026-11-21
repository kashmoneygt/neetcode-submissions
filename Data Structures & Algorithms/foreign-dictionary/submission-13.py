class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                # incorrect claim - w1 is longer than w2 and they have the same matching prefix
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # can use DFS or BFS. what we return differs based on DFS or BFS (think about 2 seperate graphs)
        # post order DFS (add result to very end because we are returning in reverse order)
        # visited, path = set(), set() # can also define visited = {} and use false = visited and true = current path
        res = []

        visited = {}  # True = in current path, False = fully processed
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
    
        res.reverse()
        return "".join(res)