# Question:
# Create a menu-driven program using a while loop.
# Keep showing the menu until the user selects option 5 (Exit).
# Menu options:
#   1. Say Hello
#   2. Print current count
#   3. Add 10 to count
#   4. Reset count
#   5. Exit
#
# Example:
#   User selects 1 -> Hello!
#   User selects 3 -> Count = 10
#   User selects 5 -> Goodbye!

count = 0

while True:
    print("\n=== MENU ===")
    print("1. Say Hello")
    print("2. Print current count")
    print("3. Add 10 to count")
    print("4. Reset count")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print(f"Current count: {count}")
    elif choice == "3":
        count = count + 10
        print(f"Added 10. Count is now: {count}")
    elif choice == "4":
        count = 0
        print("Count has been reset to 0.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1-5.")
