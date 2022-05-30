"""
TLE https://leetcode.com/submissions/detail/708711305/


"""
from __solver import *
class TrieNode:
    def __init__(self) -> None:
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word:str)->None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True
    
    def search(self, word:str)->bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isWord
    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        ans = []
        for word in words:
            trie.insert(word)

        for i in range(len(words)):
            for j in range(len(words)):
                if i!=j and trie.search(words[i]) and trie.search(words[j])\
                and str(words[i]+words[j]) == str(words[i]+words[j])[::-1]:
                    ans.append((i,j))
        return ans

# words = ["abcd","dcba","lls","s","sssll"]
words = ["bat","tab","cat"]
# words = ["a",""]
print(Solution().palindromePairs(words))