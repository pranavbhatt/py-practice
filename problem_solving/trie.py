class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False
        
class Trie:            
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        trie_root = self.root
        for c in word:
            if c not in trie_root.children:
                trie_root.children[c] = TrieNode()
            trie_root = trie_root.children[c]
        trie_root.isLeaf = True
            
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        trie_node = self.searchPrefix(word)
        if trie_node and trie_node.isLeaf:
            return True
        return False
    
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return False if not self.searchPrefix(prefix) else True
    
    def searchPrefix(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: TrieNode
        """
        trie_root = self.root
        for c in prefix:
            if c not in trie_root.children:
                return None 
            trie_root = trie_root.children[c]
        return trie_root
