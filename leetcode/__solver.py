# for Solver
import inspect
import json

# for solving problems on leetcode
from typing import *
import itertools, collections, functools
import heapq, bisect, operator
from math import *

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
            node.left = self.insertLevelOrder(rootList,2*i+1)
            node.right = self.insertLevelOrder(rootList,2*i+2)
            return node 

    def printInOrder(self,node):
        if node!=None:
            print(node.val,end=' ')
            self.printInOrder(node.left)
            self.printInOrder(node.right)

    def makeTree(self,rootList:list):
        """ https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array """
        if rootList == []:
            return TreeNode(None)
        return self.insertLevelOrder(rootList,0)


class TrieNode:
    """https://leetcode.com/submissions/detail/708492521/"""
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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printListFromNode(self) -> None:
        node = self
        if not node:
            print("End of list")
            return
        while node:
            print(node.val,end=" ")
            node = node.next
        print("\n")

class SinglyLinkedList:
    def __init__(self):
        # self.head = ListNode()
        self.head = None
        
    def initList(self,vals=[]):
        print(vals)
        # head = ListNode()
        # node = head
        # for val in vals:
        #     node.next = ListNode(val)
        #     node = node.next
        #     print(node.val)
        # return head
        self.head = ListNode(vals[0])
        node = self.head
        for val in vals[1:]:
            node.next = ListNode(val)
            node = node.next
        # self.head = head
        print(self.head.next)
        print(self.head.val,self.head.val)
        return self.head

    def printList(self) -> None:
        node = self.head
        if not node:
            print("No list")
            return
        while node:
            print(node.val,end=" ")
            node = node.next
        print("\n")

class Solver:
    """ Leetcode Solver. 
    --Runs the LAST METHOD in Solution class--
    and returns its return values.
    **TARGET METHOD MUST BE POSITIONED AT THE END** """
    def solve(Solution, sol_name, *args):
        if Solution is None or args is None:
            return ValueError
        cl = Solution
        members = inspect.getmembers(cl)
        output = None

        print(members[-5:])
        # # target function MUST ALWAYS be the last one
        # target_method = members[-1]
        for name,f in members:
            if name==sol_name:
                output = f(cl,*args)

        ret = json.dumps({
            'name':name,
            'input':str(args),
            'output':str(output)
        })
        print(ret)
        return ret
    
    def solve2(method, *args):
        print(inspect.isfunction(method),method.__class__, type(method).__class__)
        print(method.im_class.__name__)
        print(method.__qualname__)
        print(method.__name__, method.__doc__)
        spec = inspect.getfullargspec(method)
        print(spec, args)#, inspect.getclasstree(method))
        output = method(method,args)
        print(output)

# def execute(function, *args):



if __name__=="__main__":
    print(inspect.signature(Solver.solve))
    # print(Solver.solve.__setattr__('sol_name','bbb'))
    # print(Solver.solve2.__annotations__)
    # print(inspect.getmro(Solver.solve)[0].__name__)
    # Solver.solve2(TreeNode.makeTree,[1,2,3,3])