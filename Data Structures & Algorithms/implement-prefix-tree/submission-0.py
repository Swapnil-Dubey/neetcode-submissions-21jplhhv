class TrieNode:
    def __init__(self):
            self.children = {} #hashmap
            self.endofword = False

            # children["a"] = TrieNode () #is how we insert

class PrefixTree:

    def __init__(self):
        self.root = TrieNode() #empty tree
      
        

    def insert(self, word: str) -> None:
        cur = self.root
        #insert char by char in word    
        for c in word:
            if c not in cur.children: #check if this char alr exists in tree
                cur.children[c]=TrieNode()
            cur = cur.children[c]
        cur.endofword = True


    def search(self, word: str) -> bool:
        cur = self.root
        #search char by char in word    
        for c in word:
            if c not in cur.children: #check if this char alr exists in tree
                return False
            else:
                cur = cur.children[c]
        return cur.endofword        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children: #check if this char alr exists in tree
                return False
            else:
                cur = cur.children[c]
        return True
        
        