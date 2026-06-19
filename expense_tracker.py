def show_menu():
    print("\n" + "=" * 50)
    print("   📊 EXPENSE TRACKER")
    print("=" * 50)
    print("1. Add Expense")
    print("2. View Total")
    print("3. View All Expenses")
    print("4. Reset Expenses")
    print("5. Exit")
    print("=" * 50)

def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
        if amount < 0:
            print("❌ Amount cannot be negative!")
            return
        category = input("Enter category (optional): ") or "General"
        expenses.append({"amount": amount, "category": category})
        print(f"✅ Expense added: ${amount:.2f} ({category})")
    except ValueError:
        print("❌ Please enter a valid number!")

def view_total(expenses):
    if not expenses:
        print("📭 No expenses recorded yet!")
        return
    total = sum(expense["amount"] for expense in expenses)
    print(f"\n💰 Total Spent: ${total:.2f}")
    print(f"📊 Number of Expenses: {len(expenses)}")

def view_all(expenses):
    if not expenses:
        print("📭 No expenses recorded yet!")
        return
    print("\n" + "-" * 40)
    print("ALL EXPENSES".center(40))
    print("-" * 40)
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. ${expense['amount']:.2f} - {expense['category']}")
    print("-" * 40)
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total: ${total:.2f}")

def reset_expenses():
    confirm = input("Are you sure? (y/n): ")
    if confirm.lower() == 'y':
        print("✅ Expenses reset!")
        return []
    return None

def main():
    expenses = []
    print("\n" + "=" * 50)
    print("   WELCOME TO EXPENSE TRACKER")
    print("=" * 50)

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_total(expenses)
        elif choice == "3":
            view_all(expenses)
        elif choice == "4":
            result = reset_expenses()
            if result is not None:
                expenses = result
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()