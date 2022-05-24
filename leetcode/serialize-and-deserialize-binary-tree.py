"""
https://leetcode.com/submissions/detail/706120495/
"""
from __solver import *
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root==None: return ""
        serialized = []
        queue = [root]
        while queue:
            # print(queue)
            node = queue.pop(0)
            if node: 
                queue.append(node.left)
                queue.append(node.right)
                serialized.append(str(node.val)+'/')
            else:
                serialized.append("./")


            # if not node:
            #     serialized.append(".")
            #     continue
            # print(node.val, node.left, node.right)
            # serialized.append(str(node.val))
            # if node.left: queue.append(node.left)
            # else: queue.append(None)
            # if node.right: queue.append(node.right)
            # else: queue.append(None)
        return ''.join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data=="": return []
        # data = list(data)
        data = data.split("/")
        root = TreeNode(int(data[0]))
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if data[i]!=".":
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i+=1
            if data[i]!=".":
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i+=1
        return root

rootList = [1,2,3,None,None,4,5]
# rootList = [1,2,3,6,7,4,5]
rootList = []
rootList = [1,-2,3,None,None,4,5,None,None,None,None,6,7,None,None]
root = TreeNode().makeTree(rootList)
TreeNode().printInOrder(root)
ser = Codec().serialize(root)
print(ser)
deser = Codec().deserialize(ser)
print("\nser",ser,"deser")
TreeNode().printInOrder(deser)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# print(ans)


"""
ValueError: invalid literal for int() with base 10: '-'
    node.left = TreeNode(int(data[i]))
Line 44 in deserialize (Solution.py)
    ret = deser.deserialize(data)
Line 59 in __helper__ (Solution.py)
    ret = __DriverSolution__().__helper__(
Line 73 in _driver (Solution.py)
    _driver()
Line 85 in <module> (Solution.py)
"""