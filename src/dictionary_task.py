import re
from red_black_tree import RedBlackTree

class Dictionary:
    def __init__(self, filename="dictionary.txt"):
        """
        Initializes the Dictionary object.
        - Creates a new Red-Black Tree instance.
        - Stores the target filename.
        - Automatically loads existing words from the file into the tree.
        """
        self.tree = RedBlackTree()
        self.filename = filename
        self.load_from_file()

    def load_from_file(self):
        """
        Reads words from the text file and inserts them into the Red-Black Tree.
        If the file doesn't exist, it creates an empty one.
        """
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    original_line = line.strip()
                    if not original_line:
                        continue

                    # Uses RegEx to split lines by spaces, commas, hyphens, or underscores
                    words = re.split(r'[ ,\-_]+', original_line)

                    for word in words:
                        if word:
                            # Insert each word into the RBT to ensure O(log n) search time
                            self.tree.insert(word)

        except FileNotFoundError:
            # Create the file if it's missing to avoid future errors
            open(self.filename, 'w').close()

    def search_word(self, word):
        """
        Searches for a specific word in the Red-Black Tree.
        Returns: True if found, False otherwise.
        """
        result = self.tree.search(word)
        # Check if the returned node contains actual data (not a null leaf)
        return result.data is not None

    def insert_word(self, word):
        """
        Adds a new word to both the Red-Black Tree (in-memory) and the text file (storage).
        - Prevents duplicate entries.
        - Ensures the text file formatting remains clean (new line handling).
        """
        # 1. Validation: Check if the word already exists
        if self.search_word(word):
            return False, "ERROR: Word already in the dictionary!"

        # 2. Update Memory: Insert into the Red-Black Tree
        self.tree.insert(word)

        # 3. Update Storage: Append the word to the text file
        with open(self.filename, 'a+') as file:
            # Check if the file is not empty and doesn't end with a newline
            file.seek(0, 2)  # Move pointer to the end of the file
            if file.tell() > 0:
                file.seek(file.tell() - 1)
                last_char = file.read(1)
                if last_char != '\n':
                    file.write('\n')
            
            # Write the word followed by a newline
            file.write(word + "\n")

        # Return success and the updated tree statistics
        return True, self.get_stats()

    def get_stats(self):
        """
        Calculates and returns the current state of the Red-Black Tree.
        - Size: Total number of nodes.
        - Height: Total height from root to deepest leaf.
        - Black Height: Number of black nodes from root to leaves.
        """
        return {
            "size": self.tree.size,
            "height": self.tree.get_height(self.tree.root),
            "black_height": self.tree.get_black_height(self.tree.root)
        }