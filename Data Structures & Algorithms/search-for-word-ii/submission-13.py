class Node:
    def __init__(self, eow:bool=False):
        self.children = {}
        self.eow = eow
    
    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for word in words:
            root.add(word)
        
        ROWS, COLS = len(board), len(board[0])
        res, seen = set(), set()
        
        def dfs(r, c, curr, word):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in seen or board[r][c] not in curr.children:
                return
            
            seen.add((r, c))
            curr = curr.children[board[r][c]]
            word += board[r][c]
            if curr.eow:
                res.add(word)
            
            dfs(r - 1, c, curr, word)
            dfs(r + 1, c, curr, word)
            dfs(r, c - 1, curr, word)
            dfs(r, c + 1, curr, word)

            seen.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)