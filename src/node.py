class Node:
    def __init__(self, data, color="RED"):
        """
        Represents a single node within the Red-Black Tree.
        """
        # The actual value stored in the node (e.g., a word string)
        self.data = data
        
        # Red-Black Tree property: New nodes are usually inserted as "RED" 
        # to minimize the number of black-height violations.
        self.color = color  # Should be either "RED" or "BLACK"
        
        # Pointers to the left and right children (initially None/Null)
        self.left = None
        self.right = None
        
        # Pointer to the parent node; essential for performing 
        # tree rotations and re-balancing during insertions.
        self.parent = None