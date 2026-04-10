from node import Node

class RedBlackTree:
    def __init__(self):
        """
        Initializes the Red-Black Tree.
        - T_nil: A special 'sentinel' node representing leaf nodes (always BLACK).
        - root: Initially points to T_nil.
        - size: Keeps track of the total word count.
        """
        self.T_nil = Node(None, color="BLACK")
        self.root = self.T_nil
        self.size = 0

    def left_rotate(self, x):
        """
        Moves node 'x' down and its right child 'y' up to become the new parent.
        Essential for maintaining tree balance.
        """
        y = x.right
        x.right = y.left  # Turn y's left subtree into x's right subtree
        if y.left != self.T_nil:
            y.left.parent = x
        
        y.parent = x.parent # Link x's parent to y
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x  # Put x on y's left
        x.parent = y

    def right_rotate(self, y):
        """
        Moves node 'y' down and its left child 'x' up to become the new parent.
        The mirror image of a left rotation.
        """
        x = y.left
        y.left = x.right # Turn x's right subtree into y's left subtree
        if x.right != self.T_nil:
            x.right.parent = y
        
        x.parent = y.parent # Link y's parent to x
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        
        x.right = y # Put y on x's right
        y.parent = x

    def insert(self, key):
        """
        Standard BST insertion, followed by Red-Black Tree fixing.
        """
        new_node = Node(key)
        new_node.left = self.T_nil
        new_node.right = self.T_nil
        
        y = None
        x = self.root
        
        # Traverse down to find the correct insertion point
        while x != self.T_nil:
            y = x
            if new_node.data < x.data:
                x = x.left
            else:
                x = x.right
        
        new_node.parent = y
        if y == None:
            self.root = new_node # Tree was empty
        elif new_node.data < y.data:
            y.left = new_node
        else:
            y.right = new_node
        
        # Case: Root must always be Black
        if new_node.parent == None:
            new_node.color = "BLACK"
            self.size += 1
            return
            
        # Case: If grandparent doesn't exist, no balancing needed yet
        if new_node.parent.parent == None:
            self.size += 1
            return

        # Fix any property violations (like two RED nodes in a row)
        self.fix_insert(new_node)
        self.size += 1

    def fix_insert(self, k):
        """
        Restores RBT properties after insertion by recoloring or rotating.
        Loops while there is a 'Double Red' violation.
        """
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Uncle node
                if u.color == "RED":
                    # Case 1: Uncle is Red -> Recolor only
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    # Case 2/3: Uncle is Black -> Rotations needed
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)
            else:
                # Mirror cases when parent is the left child
                u = k.parent.parent.right 
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK" # Rule: Root is always black

    def search(self, k):
        """Public method to search for a key."""
        return self._search_recursive(self.root, k)

    def _search_recursive(self, node, k):
        """Recursive helper for O(log n) search."""
        if node == self.T_nil or k == node.data:
            return node
        if k < node.data:
            return self._search_recursive(node.left, k)
        return self._search_recursive(node.right, k)

    def get_height(self, node):
        """Calculates total tree height (Longest path from root)."""
        if node == self.T_nil:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_black_height(self, node):
        """Calculates the black-height (number of black nodes to the leaves)."""
        if node == self.T_nil:
            return 0
        left_bh = self.get_black_height(node.left)
        # If current node is black, increment the count
        if node.color == "BLACK":
            return left_bh + 1
        return left_bh

    def print_tree(self, node, indent="", last=True):
        """Visualizes the tree structure in the console."""
        if node != self.T_nil:
            print(indent, end="")
            if last:
                print("R---- ", end="")
                indent += "     "
            else:
                print("L---- ", end="")
                indent += "|    "

            color = "RED" if node.color == "RED" else "BLACK"
            print(f"{node.data} ({color})")
            
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)
