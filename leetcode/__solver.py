# for Solver
import inspect
import json

# for solving problems on leetcode
from typing import *
import itertools, collections
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insertLevelOrder(self,rootList,i):
        # level order insert
        if i<len(rootList) and rootList[i] != None:
            tmp = TreeNode(rootList[i],None,None)
            node = tmp
            node.left = self.insertLevelOrder(TreeNode, rootList,2*i+1)
            node.right = self.insertLevelOrder(TreeNode, rootList,2*i+2)
            return node 

    def printInOrder(self,node):
        if node!=None:
            print(node.val)
            self.printInOrder(self,node.left)
            self.printInOrder(self,node.right)

    def makeTree(self,rootList:list):
        """ https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array """
        return self.insertLevelOrder(TreeNode,rootList,0)

class Solver:
    """ Leetcode Solver. 
    Runs the LAST METHOD in Solution class 
    and returns its return values.
    **TARGET METHOD MUST BE POSITIONED AT THE END** """
    def solve(Solution, *args):
        if Solution is None or args is None:
            return
        cl = Solution
        members = inspect.getmembers(cl)

        # target function MUST ALWAYS be the last one
        target_method = members[-1]
        (name, f) = target_method
        _output = f(cl,*args)

        ret = json.dumps({
            'name':name,
            'input':str(args),
            'output':str(_output)
        })
        print(ret)
        return ret