while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter by Category")
    print("4. View Summary")
    print("5. Exit")

    choice=input("Enter your choice (1-5):")
    if(choice=="1"):
        addexpense()
    elif(choice=="2"):
        viewexpense()
    elif(choice=="3"):
        filterexpense()
    elif(choice=="4"):
        viewexpense()
    elif(choice=="5"):
        print("exiting application and good bye")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")