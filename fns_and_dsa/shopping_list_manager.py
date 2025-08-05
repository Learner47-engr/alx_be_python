def shopping_list_manager():
    """
    Manages a shopping list by allowing users to add, remove, view, and exit.
    """
    shopping_list = []

    while True:
        print("\n--- Shopping List Manager ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")
        
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' was not found in the list.")

        elif choice == '3':
            print("\n--- Your Shopping List ---")
            if not shopping_list:
                print("The list is empty.")
            else:
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
        
        elif choice == '4':
            print("Exiting shopping list manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    shopping_list_manager()