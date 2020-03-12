class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={}
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        k=self.root
        for i in range(len(word)):
            if word[i] not in k:
                k[word[i]]={}
            if(i==len(word)-1):
                s=k[word[i]]
                s['end']='True'
            k=k[word[i]]    

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        k=self.root
        for i in word:
            if i not in k:
                return False
            k=k[i]
        if 'end' not in k:
            return False
        else:
            return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        k=self.root        
        for i in prefix:
            if i not in k:
                return False
            k=k[i]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)