import pandas as pd

def main_menu():
    # keep track of invalid inputs
    invalid_count = 0

    def show_data_summary():
        df = pd.read_csv("pandas-analysis/cleaned_sales_data.csv")
        print(df.describe())

    def show_average_transaction_amount():
        df = pd.read_csv("pandas-analysis/cleaned_sales_data.csv")
        average_amount = df["Amount"].mean()
        print(f"Average Transaction Amount: {average_amount}")

    while True:
        print("\n--- Main Menu ---")
        print("1. Greet User")
        print("2. Show Data Summary")
        print("3. Show Average Transaction Amount")
        print("4. Exit")

        choice = input("Enter your choice (1-3)")

        if choice == "1":
            print("hello, there!")
        elif choice == "2":
            show_data_summary()
        elif choice == "3":
            show_average_transaction_amount()
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Please select 1, 2, or 3")
            invalid_count += 1
            if invalid_count >= 3:
                print("Too many invalid attempts. Start over.")
                break
        
main_menu()
