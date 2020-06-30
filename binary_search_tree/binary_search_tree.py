"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
        
        return self

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        found = False
        if self.value < target:
            if self.left is None:
                return False
        found = self.left.contains(target)

        if self.value >= target:
            if self.right is None:
                return False
        found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        fn(self.value)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        queue = []
        # add the first node to the queue
        queue.append(node)
        # while queue is not empty
        while len(queue) is not 0:
            first_node = queue[0]
            # remove the first node from the queue
            queue.pop(0)
            # print the removed node
            print(first_node.value)
            # add all children into the queue    
            if first_node.left:
                queue.append(first_node.left)
            if first_node.right:
                queue.append(first_node.right)
    
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        stack = []
        # add the first node the the stack
        stack.append(node)
        # while the stack is not empty
        while len(stack) is not 0:
            # get the current node from the top of the stack
            top = stack[-1]
            stack.pop(len(stack)-1)
            # print that node
            print(top.value)
            # add all the children to the stack, order matters
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BSTNode(1)
nodes = [8,5,7,6,3,4,2]

for n in nodes:
    bst.insert(n)

# print_node = lambda x: print(x)
# bst.for_each(print_node)

bst.dft_print(bst)