class Node:
    def __init__(self, eow=False):
        self.children = {}
        self.eow = eow

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]

        curr.eow = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                elif c not in curr.children:
                    return False
                curr = curr.children[c]
            
            return curr.eow

        return dfs(0, self.root)