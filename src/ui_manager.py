from dictionary_task import Dictionary

class UIManager:
    def __init__(self):
        """
        Initializes the User Interface Manager.
        It creates an instance of the Dictionary, which handles the 
        Red-Black Tree and file I/O.
        """
        self.my_dict = Dictionary()

    def show_menu(self):
        """
        Displays the main command-line interface menu to the user.
        """
        print("\n--- English Dictionary Menu ---")
        print("1. Search for a word")
        print("2. Insert a new word")
        print("3. Print Tree Stats")
        print("4. Visual Tree Structure")
        print("5. Exit")

    def run(self):
        """
        The main control loop of the application.
        It keeps the program running and responds to user inputs.
        """
        while True:
            self.show_menu()
            choice = input("Choose an option: ")

            # --- Option 1: SEARCH ---
            if choice == '1':
                word = input("Enter word to search: ").strip()
                # Calls the dictionary search logic (O(log n) efficiency)
                if self.my_dict.search_word(word):
                    print("YES")
                else:
                    print("NO")

            # --- Option 2: INSERT ---
            elif choice == '2':
                word = input("Enter word to insert: ").strip()
                # Returns success status and updated tree stats
                success, result = self.my_dict.insert_word(word)
                if success:
                    print("Inserted.")
                    print(f"Size: {result['size']}")
                    print(f"Height: {result['height']}")
                    print(f"Black Height: {result['black_height']}")
                else:
                    # Prints the error message if the word already exists
                    print(result)

            # --- Option 3: STATS ---
            elif choice == '3':
                # Displays size, height, and black-height
                print(f"Current Stats: {self.my_dict.get_stats()}")

            # --- Option 4: VISUALIZE ---
            elif choice == '4':
                print("\n--- Visual Tree Structure ---")
                # Calls the recursive print function to show tree branches
                self.my_dict.tree.print_tree(self.my_dict.tree.root)

            # --- Option 5: EXIT ---
            elif choice == '5':
                print("Exiting...")
                break # Breaks the while loop to end the program
          
            # --- ERROR HANDLING ---
            else:
                print("Invalid choice, please try again.")