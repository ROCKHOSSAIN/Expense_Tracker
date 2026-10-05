from src.tracker import (
    set_monthly_budget,
    add_expense, 
    view_expenses, 
    filter_expenses, 
    get_summary, 
    delete_expense
)

while True:
    print("\n==============================")
    print("      💰 EXPENSE TRACKER      ")
    print("==============================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter by Category")
    print("4. View Summary")
    print("5. Delete Expense")
    print("6. Exit")
    print("==============================")

    choice = input("Enter your choice (1-6): ").strip()
    if choice == "0":
        print("monthly budget:")
        set_monthly_budget()
    if choice == "1":
        print("\n--- Add New Expense ---")
        try:
            amount = float(input("Expense Amount (BDT): "))
            if amount < 0:
                print("Amount cannot be negative!")
                continue
            category = input("Enter category (e.g., Food, Transport): ").strip()
            note = input("Enter note/description: ").strip()
            add_expense(amount, category, note)
        except ValueError:
            print("Invalid input! Please enter a valid number for amount.")

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        filter_choice = input("\nEnter category name to filter: ").strip()
        filter_expenses(filter_choice)

    elif choice == "4":
        get_summary()

    elif choice == "5":
        delete_expense()
        
    elif choice == "6":
        print("\nExiting application. Goodbye!")
        break
    
        
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")