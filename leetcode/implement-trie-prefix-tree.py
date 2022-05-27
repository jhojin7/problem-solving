"""
https://leetcode.com/submissions/detail/708492521/
"""
from __solver import *

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        print(word)        
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True
        # for ch in word:
        #     if ch not in node.children.keys():
        #         node.children[ch] = TrieNode()
        #         node.children[ch].char = ch
        #         return True
        #     node = node.children[ch]
        
    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children.keys():
                return False
            node = node.children[ch]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children.keys():
                return False
            node = node.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("hello")
obj.insert("hella")
obj.insert("hellb")
obj.insert("hellc")
obj.insert("helba")
obj.insert("helaa")
obj.insert("hexla")
param_2 = obj.search("hella")
param_3 = obj.startsWith("hel")
print(param_2, param_3)
param_2 = obj.search("hell")
param_3 = obj.startsWith("ello")
print(param_2, param_3)