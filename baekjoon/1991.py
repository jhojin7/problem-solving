"""
id: 1991
title:트리순회
ac:https://www.acmicpc.net/source/44789456 
"""
import sys
from io import StringIO
sys.stdin = StringIO("""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
""".strip())


class TreeNode:
    def __init__(self, ch, left=None, right=None) -> None:
        self.ch = ch
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return "TreeNode(ch={},left={},right={})".format(
            self.ch, self.left, self.right)

def make_tree(n):
    node = TreeNode(n)
    l,r = nodes[n]
    if l != '.': 
        node.left = make_tree(l)
    if r != '.': 
        node.right = make_tree(r)
    return node

def preorder(node):
    print(node.ch,end='')
    if node.left != None:
        preorder(node.left)
    if node.right != None:
        preorder(node.right)
    return 

def inorder(node):
    if node.left != None:
        inorder(node.left)
    print(node.ch,end='')
    if node.right != None:
        inorder(node.right)
    return 

def postorder(node):
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    print(node.ch,end='')
    return 

import sys
nodes = {}
N = int(input())
for _ in range(N):
    n,l,r = input().split()
    nodes[n] = (l,r)

root = make_tree('A')
preorder(root);print()
inorder(root);print()
postorder(root);print()