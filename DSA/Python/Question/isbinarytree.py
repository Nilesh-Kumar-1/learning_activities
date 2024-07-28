# For the purposes of this challenge, we define a binary search tree to be a binary tree with the following properties:

#     The 

# value of every node in a node's left subtree is less than the data value of that node.
# The
# value of every node in a node's right subtree is greater than the data value of that node.
# The
# value of every node is distinct.
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_node(self, val):
        if val <= self.val and self.left:
            self.left.insert_node(val)
        elif val <= self.val:
            self.left = TreeNode(val)
        elif val > self.val and self.right:
            self.right.insert_node(val)
        else:
            self.right = TreeNode(val)
    def bfs(self):
        queue = Queue()
        queue.put(self)
        tree=[]

        while not queue.empty():
            current_node = queue.get()
            tree+=[current_node.val]

            if current_node.left:
                queue.put(current_node.left)

            if current_node.right:
                queue.put(current_node.right)
        return tree
    
def checkBST(root):
    if root is None:
        return True
    # elif root.val>root.left or root.val<root.right 