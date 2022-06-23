"""
id: 2263
title:트리의순회
ac:https://www.acmicpc.net/source/44931088
"""
import sys
from io import StringIO
sys.stdin = StringIO("""

""".strip())

import sys
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, val, right=None, left=None) -> None:
        self.val = val
        self.right = right
        self.left = left

def preorder(root:TreeNode):
    print(root.val,end=' ')
    if root.left: preorder(root.left)
    if root.right: preorder(root.right)
    return

def makeTreeIdx(start, end):
    if end-start != 0:
        index = inorder.index(postorder.pop())
        val = inorder[index]
        node = TreeNode(val)
        node.right = makeTreeIdx(index+1,end)
        node.left = makeTreeIdx(start,index)
        return node

N = int(input())
inorder = list(map(int,sys.stdin.readline().split()))
postorder = list(map(int,sys.stdin.readline().split()))

root = makeTreeIdx(0,N)
preorder(root)