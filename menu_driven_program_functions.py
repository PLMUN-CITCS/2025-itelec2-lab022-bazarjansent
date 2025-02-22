def display_menu() -> None:
    """
    Displays the program's menu options to the user.
    """
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def greet_user() -> None:
    """
    Prints a greeting message.
    """
    print("Hello! Welcome!")

def even_odd_checker_action() -> None:
    """
    Handles input and checks if the entered number is even or odd.
    """
    while True:
        try:
            number = int(input("Enter an integer: ").strip())
            if number % 2 == 0:
                print(f"{number} is an Even number.")
            else:
                print(f"{number} is an Odd number.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def handle_menu_choice(choice: int) -> bool:
    """
    Executes the corresponding action based on the user's menu choice.
    Args:
        choice (int): The menu option selected by the user.
    Returns:
        bool: True if the user chooses to exit, False otherwise.
    """
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Invalid choice. Please select a valid option (1-3).")
    return False

def main() -> None:
    """
    Main function to execute the menu-driven program.
    """
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): ").strip())
            if handle_menu_choice(choice):
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
