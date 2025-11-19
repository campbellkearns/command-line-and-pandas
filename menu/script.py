def main_menu():
    # keep track of invalid inputs
    invalid_count = 0

    while True:
        print("\n--- Main Menu ---")
        print("1.Greet User")
        print("2. Show Data Summary")
        print("3. Exit")

        choice = input("Enter your choice (1-3)")

        if choice == "1":
            print("hello, there!")
        elif choice == "2":
            print("This is a sample CLI tool")
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Please select 1, 2, or 3")
            invalid_count += 1
            if invalid_count >= 3:
                print("Too many invalid attempts. Start over.")
                break
        
main_menu()