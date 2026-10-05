import json
import os
from datetime import datetime

FILE_NAME = "expense.json"


def load_expense():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# শুরুতেই ফাইল থেকে ডাটা লোড করা হচ্ছে (আগের ওভাররাইট বাগটি ঠিক করা হয়েছে)
all_expenses = load_expense()

def save_expense():
    with open(FILE_NAME, "w") as file:
        json.dump(all_expenses, file, indent=4)

def set_monthly_budget():
    try:
        budget = float(input("\nEnter your monthly budget amount: "))
        print(f"Budget set to {budget} BDT successfully!")
    except ValueError:
        print("Please enter a valid number.")


def add_expense(amount, category, note):
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date_str
    }
    all_expenses.append(expense)
    save_expense()
    print("\n✅ Success: Expense has been added successfully!")

def view_expenses():
    if not all_expenses:
        print("\n📭 No expenses recorded yet!")
        return
    
    print("\n" + "="*50)
    print(f"{'No.':<4} | {'Date & Time':<17} | {'Category':<12} | {'Amount':<8} | {'Note'}")
    print("="*50)
    for i, exp in enumerate(all_expenses, start=1):
        print(f"{i:<4} | {exp['date']:<17} | {exp['category']:<12} | {exp['amount']:<8} | {exp['note']}")
    print("="*50)

def filter_expenses(category_name):
    filtered = [exp for exp in all_expenses if exp['category'].lower() == category_name.lower()]
    
    if not filtered:
        print(f"\n No expenses found in category: '{category_name}'")
        return
    
    print("\n" + "="*45)
    print(f"--- Expenses in Category: '{category_name.capitalize()}' ---")
    print(f"{'No.':<4} | {'Date & Time':<17} | {'Amount':<8} | {'Note'}")
    print("="*45)
    for i, exp in enumerate(filtered, start=1):
        print(f"{i:<4} | {exp['date']:<17} | {exp['amount']:<8} | {exp['note']}")
    print("="*45)

def delete_expense():
    if not all_expenses:
        print("\n📭 No expenses to delete!")
        return
    
    view_expenses()
    try:
        index = int(input("\nEnter the number of the expense to delete: ")) - 1
        if 0 <= index < len(all_expenses):
            removed = all_expenses.pop(index)
            save_expense()
            print(f"\n Deleted successfully: {removed['note']} ({removed['amount']} BDT)")
        else:
            print("\n Invalid index number! Please try again.")
    except ValueError:
        print("\n Error: Please enter a valid number!")

def get_summary():
    if not all_expenses:
        print("\n No expenses available for summary!")
        return
        
    total_amount = sum(exp['amount'] for exp in all_expenses)
    print("\n" + "--- 📊 Expense Summary ---")
    print(f"💰 Total Expenses        : {total_amount:.2f} BDT")
    print(f"📝 Total Transactions    : {len(all_expenses)}")
    print("----------------------------")