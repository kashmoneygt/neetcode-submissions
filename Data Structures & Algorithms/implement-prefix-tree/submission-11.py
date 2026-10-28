class Node:
    def __init__(self, eow: bool = False):
        self.children = {}
        self.eow = eow

class PrefixTree:

    def __init__(self):
        self.trie = Node()

    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]

        cur.eow = True


    def search(self, word: str) -> bool:
        cur = self.trie
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.eow
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True
        