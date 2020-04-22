import sys
sys.path.append('G:/Data/Lambda/CS/Data-Structures/queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

    # Insert the given value into the tree
    def insert(self, value):
        compare_node = self
        while True:
            if value > compare_node.value:
                if compare_node.right:
                    compare_node = compare_node.right
                else:
                    compare_node.right = BinarySearchTree(value)
                    break
            elif value < compare_node.value:
                if compare_node.left:
                    compare_node = compare_node.left
                else:
                    compare_node.left = BinarySearchTree(value)
                    break
            elif value == compare_node.value:
                
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current_node = self
        while True:
            if current_node == None:
                return False
            elif current_node.value > target:
                current_node = current_node.left
                continue
            elif current_node.value < target:
                current_node = current_node.right
                continue
            elif current_node.value == target:
                return True
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = 0
        current_node = self
        while current_node != None:
            max_value = current_node.value
            current_node = current_node.right
        return max_value 

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self,node=None):
        # if I can go left go left
        # you get to the lowest value
        
        # from there print value, then go up
        # print the parent then go right once
        # then keep going left until go can't
        
        # then go up one right one 
        # keep going left until you can't. 
        if node is None:
            node = self
        if node.left:
            node.left.in_order_print(node.left)
        print(self.value)
        if node.right:
            node.right.in_order_print(node.right)
        pass
    
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node == None:
        print(self.value)
        print()
        # print self, left right, then print
        # lr of the left then lr of the right
        # and so forth 
        # we are printing horizontally at every level.
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
