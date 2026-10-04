all_expenses=[]
def add_expense(amount,category,note):
    global all_expenses
    expense={
        "amount":amount,
        "category":category,
        "note":note,
    }
    all_expenses.append(expense)
    print("expense has been added successfully!")
print(all_expenses)
