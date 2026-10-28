class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # to hold c1 -> nei where w1 comes before all nei
        adj = { c : set() for word in words for c in word }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            
            # handle edge case for invalid ordering
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen): # find first differing char
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) # w1[j] before w2[j]
                    break

        visited = {} # False = visited, True = visited and in cur path
        res = []

        def dfs(c) -> bool:
            if c in visited:
                # if our visited returns True, we saw this char before -> cycle
                return visited[c] 

            visited[c] = True # visited and in cur path

            for nei in adj[c]:
                if dfs(nei):
                    return True # our nei is part of cycle

            visited[c] = False # visited but not in cur path (like backtracking)
            res.append(c)
            return False

        for c in adj.keys():
            if dfs(c):
                return ""
        
        return "".join(res[::-1])
