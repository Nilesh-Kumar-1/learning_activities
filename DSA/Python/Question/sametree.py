# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same val

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

def isSameTree(p, q) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None or p.val != q.val:
            return False
        # print("p ==",p.bfs())
        # # p.bfs()
        # print("q==",q.bfs())
        # q.bfs()
        print(isSameTree(p.right,q.right),isSameTree(p.left,q.left))
        
        return (isSameTree(p.right,q.right) and isSameTree(p.left,q.left))

ele1=list(range(10,100,10))
p= TreeNode(10)
q=TreeNode(10)

insert_element=[50]
for i in insert_element:
    p.insert_node(i)
    q.insert_node(i)
# a=sol
print(isSameTree(p,q))


