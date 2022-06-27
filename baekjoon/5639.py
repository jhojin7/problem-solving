"""
id: 5639
title:이진검색트리
ac:https://www.acmicpc.net/source/45119049
"""
import sys
from io import StringIO

sys.stdin = StringIO("""
10
5
3
1
2
11
12
18
15
20
""".strip())
# 50
# 30
# 24
# 5
# 28
# 45
# 98
# 52
# 60

# class TreeNode:
#     def __init__(self, val, left=None, right=None) -> None:
#         self.val = val
#         self.left = left
#         self.right = right

# def postorder(node):
#     if node.left: postorder(node.left)
#     if node.right: postorder(node.right)
#     print(node.val)

# def make_tree(start,end)->TreeNode:
#     # stop recursion
#     if end-start != 0:
#         # find subroot index
#         idx = -1
#         for i in range(start+1,end):
#             # print(">>",preorder[i], preorder[start])
#             if preorder[i] >= preorder[start]:
#                 idx = i
#                 break
#         if idx == -1:
#             idx = end
#         # print(start, end, idx,preorder[start])
#         # print(preorder[start],preorder[start+1:idx], preorder[idx:end])

#         # make subroot node
#         node = TreeNode(preorder[start])
#         # print(start+1,idx,end, len(preorder[idx:end]))

#         # left
#         if idx-start-1 > 0:
#             node.left = make_tree(start+1, idx)
#         # right
#         if end-idx > 0:
#             node.right = make_tree(idx, end)
#         return node

import sys
sys.setrecursionlimit(10000) # ...

def postorderTree(start, end):
    # print(preorder[start:end])
    if end-start <= 0: return

    # find subroot index
    idx = -1
    for i in range(start+1,end):
        if preorder[i] >= preorder[start]:
            idx = i
            break
    if idx == -1:
        idx = end

    # print(preorder[start+1:idx],preorder[idx:end])
    postorderTree(start+1,idx)
    postorderTree(idx,end)
    sys.stdout.write(str(preorder[start])+"\n")
    # print(preorder[start])
    return

input = sys.stdin.readline
preorder = []
while True:
    try: 
        x = int(input())
        preorder.append(x)
    except: break
# print(preorder)
postorderTree(0,len(preorder))

