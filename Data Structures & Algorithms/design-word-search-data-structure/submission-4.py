class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.eow = True

    def search(self, word: str) -> bool:

        def dfs(i, root):
            cur = root
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                elif c not in cur.children:
                    return False
                else:
                    cur = cur.children[c]
        
            return cur.eow
        
        return dfs(0, self.root)
