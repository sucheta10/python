from expense import Expense

def get_user_expense():
    print(f"📍 Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_date = input("Enter expense date (YYYY-MM-DD) or leave empty for today: ")

#check if expense_date is not provided or is a falsy value (e.g., an empty string). If true, expense_date is set to None. This ensures that expense_date has a valid value, either a date or None.

    if not expense_date:
        expense_date = None

    print(f"You've entered {expense_name}, {expense_amount}, {expense_date}")
   #list
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    while True:  #infinite loop that will continue until a valid category is selected.
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):  #The enumerate function in Python is used to iterate over a list (or any other iterable) and keep track of the index of the current item in the loop.
            print(f" {i + 1}. {category_name}")
#creates a string value_range that represents the valid range of input values, which is from 1 to the length of the expense_categories list.
        value_range = f"[1 - {len(expense_categories)}]"

        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount, date=expense_date)
            return new_expense
        else:
            print("Invalid category. Please try again!")
