def display_menu():
    """Displays the main menu options."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """Runs the shopping list manager application."""
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        # Check if input is a number
        if not choice.isdigit() or not 1 <= int(choice) <= 4:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        if int(choice) == 1:
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"Added '{item}' to the shopping list.")

        elif int(choice) == 2:
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif int(choice) == 3:
            # Display the shopping list
            if shopping_list:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Shopping list is empty.")

        elif int(choice) == 4:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()