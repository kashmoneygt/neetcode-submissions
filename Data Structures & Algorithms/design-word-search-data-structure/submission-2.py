class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # exact same as insert() in "Implement Trie" problem
        # O(n)
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(j, root): # j represents which letter we're trying to match
            cur = root # used to be self.root
            for i in range(j, len(word)):
                c = word[i]
                
                if c == ".":
                    for child in cur.children.values():
                        # it's not easy to consider all letters iteratively
                        # so we encapsulated our logic in a dfs() method
                        if dfs(i + 1, child):
                            return True
                    
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord

        return dfs(0, self.root)
