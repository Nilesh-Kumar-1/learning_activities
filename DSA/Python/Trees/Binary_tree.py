from queue import Queue


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    # Here are the rules:

    # If the current node doesn’t have a left child, we just create a new nodeand 
    # set it to the current node’s left_child.
    # If it does have the left child, we create a new node and put it in the current left child’s place. 
    # Allocate this left child node to the new node’s left child.

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    #DFS: pre-order, in-order, and post-order.

    def pre_order(self): # Print middle,left, right
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()

    def in_order(self): # Print left, middle, right
        if self.left_child:
            self.left_child.in_order()
        print(self.value)

        if self.right_child:
            self.right_child.in_order()

    def post_order(self): # print left right middle
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.value)

    # BFS algorithm traverses the tree level by level and depth by depth
    # Algo 
    # First add the root node into the queue with the put method.
    # Iterate while the queue is not empty.
    # Get the first node in the queue, and then print its value.
    # Add both left and right children into the queue (if the current nodehas children).
    # Done. We will print the value of each node, level by level, with our queuehelper.
    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)

            if current_node.left_child:
                queue.put(current_node.left_child)

            if current_node.right_child:
                queue.put(current_node.right_child)

    #bst --> left<middle(root)<right
    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinaryTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinaryTree(value)

    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value
    
    def remove_node(self, value, parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            #1: A node with no children (leaf node).
            # If the node we want to delete has no children, we simply delete it. The algorithm doesn’t need to reorganize the tree.
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            #2: A node with just one child (left or right child).
            #        |50|                              |50|
            #      /      \                           /    \
            #    |30|     |70|   (DELETE 30) --->   |20|   |70|
            #   /            
            # |20|
            # In this case, our algorithm needs to make the parent of the node point to the child node. 
            # If the node is the left child, we make the parent of the left child point to the child.
            # If the node is the right child of its parent, we make the parent of the right child point to the child.
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            #3: A node with two children.

            #        |50|                              |50|
            #      /      \                           /    \
            #    |30|     |70|   (DELETE 30) --->   |40|   |70|
            #   /    \                             /
            # |20|   |40|                        |20|

            # When the node has 2 children, we need to find the node with the minimum value, starting from the node’s right child. 
            # We will put this node with minimum value in the place of the node we want to remove.
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)

            return True
        
    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value

a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

print(a_node.value) # a
print(b_node.value) # b
print(c_node.value) # c
print(d_node.value) # d
print(e_node.value) # e
print(f_node.value) # f

bst=BinaryTree(15)
insert_element=[10,8,12,20,17,25,19]
for i in insert_element:
    bst.insert_node(i)

bst.bfs()

test_element=insert_element+[233,56,19]
for i in test_element:
    print(bst.find_node(i), f"for {i}")