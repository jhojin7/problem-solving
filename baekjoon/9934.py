"""
id: 9934
title:완전이진트리
ac:https://www.acmicpc.net/source/44698449
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
2
2 1 3
""".strip())

import sys, collections
class TreeNode:
    def __init__(self, val=None) -> None:
        self.val = val
        self.left = None
        self.right = None

def level_order(_nodes, half):
    # print(_nodes[half], half)
    node = TreeNode(_nodes[half])
    if len(_nodes) == 1:
        node.left = node.right = None
        return node
    node.left = level_order(_nodes[:half],half//2)
    node.right = level_order(_nodes[half+1:],half//2)
    return node

K = int(input())
# inorder binary tree
nodes = list(map(int,sys.stdin.readline().split()))
# print(K,nodes)

# change to level order
half = len(nodes)//2
root = level_order(nodes,half)

# traverse root
queue = collections.deque([root])
level_ordered = []
while queue:
    node = queue.popleft()
    level_ordered.append(node.val)
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
# print(level_ordered)

# print with level
i = 0
for depth in range(K):
    lvl = []
    for _ in range(2**depth):
        lvl.append(level_ordered[i])
        i+=1
    print(*lvl,sep=' ')