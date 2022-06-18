"""
id: 5670
title:휴대폰자판
ac: https://www.acmicpc.net/source/44679037
"""
import sys
from io import StringIO
# 4
# hello
# hell
# heaven
# goodbye
sys.stdin = StringIO("""
4
hello
hell
heaven
goodbye
3
hi
he
h
7
structure
structures
ride
riders
stress
solstice
ridiculous
""".strip())
# 7
# structure
# structures
# ride
# riders
# stress
# solstice
# ridiculous

import collections
class TrieNode:
    def __init__(self, ch='') -> None:
        self.ch = ch
        self.isWord = False
        self.children = collections.defaultdict()

    def __repr__(self) -> str:
        return "TrieNode(ch={},isWord={},children={})".format(
            self.ch, self.isWord, len(self.children)
        )

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word:str):
        word = list(word)
        # print(word)
        node = self.root
        while word:
            ch = word.pop(0)
            if ch not in node.children:
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]
        node.isWord = True
        # print(node)
        return node.isWord
    
    def search(self, word:str):
        queue = collections.deque(word)
        # print(queue)
        node = self.root
        cnt = 1
        while queue:
            ch = queue.popleft()
            node = node.children[ch]
            # print(cnt, node)
            # print(node.children)
            if len(node.children) > 1: cnt += 1
            if node.isWord:
                # even if isWord==True, if queue not empty, keep going
                if queue:
                    cnt += 1
                    # if cnt++ was done above, don't repeat
                    if len(node.children) > 1: cnt -= 1
                else:
                    # if cnt++ was done above, don't repeat
                    if len(node.children) > 1: cnt -= 1
                    # print("search:",word,queue, cnt)
                    return cnt
        return False

while True:

    try:
        N = int(input())
    except Exception:
        exit()

    # N = int(input())
    t = Trie()
    words = []
    for _ in range(N):
        word = input()
        words.append(word)
        t.insert(word)

    ans = 0
    for word in words:
        cnt = t.search(word)
        # print(cnt)
        if cnt: ans += cnt
    print("%.2f"%(ans/N))