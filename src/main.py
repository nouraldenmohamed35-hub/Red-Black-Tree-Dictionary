from ui_manager import UIManager

# The entry point of the script
if __name__ == "__main__":
    """
    This block ensures that the code inside only runs if the script 
    is executed directly, and not when imported as a module in another file.
    """
    
    # 1. Instantiate the UI Manager
    # This creates the main window and initializes the Dictionary/RBT logic.
    app = UIManager()
    
    # 2. Launch the Application
    # This starts the GUI event loop (e.g., tkinter's mainloop), 
    # keeping the window open and responsive to user input.
    app.run() 
