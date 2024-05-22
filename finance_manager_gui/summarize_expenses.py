import sqlite3
from expense import Expense
import calendar
import datetime



def summarize_expenses(expense_file_path, budget):
    print(f"📍 Summarizing User Expense from SQLite database")
    conn = sqlite3.connect(expense_file_path)
    c = conn.cursor()   #c is a cursor object
    c.execute("SELECT * FROM expenses")
    expenses = []
    for row in c.fetchall():    # this line creates a new Expense object named line_expense using the data from the current row:
        line_expense = Expense(
            name=row[0], amount=float(row[1]), category=row[2], date=row[3]  #name->1st element from row, amount->2nd,category->3rd,date->4th
        )
        expenses.append(line_expense) #adds the newly created line_expense object to the expenses list.
    conn.close()

    amount_by_category = {}  #initializes an empty dictionary amount_by_category to store the total amount spent in each category.
    for expense in expenses:  #iterates over each expense in the expenses list.
        key = expense.category  #assigns the category of the current expense to the variable key
        if key in amount_by_category:  #If key is present, the amount of the current expense is added to the existing total for that category.
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount  #If key is not present, a new entry is created in the dictionary with the category as the key and the amount of the current expense as the value.
    summary = "Expenses By Category📈:\n"
    for key, amount in amount_by_category.items():
        summary += f" {key}: ${amount:.2f}\n"

    total_spent = sum([x.amount for x in expenses])  #calculates the total amount spent by summing the amount attribute of each expense in the expenses list
    summary += (f"💸 Total Spent: ${total_spent:.2f}\n")

    remaining_budget = budget - total_spent
    summary += (f"✅ Remaining Budget: ${remaining_budget:.2f} !\n")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    summary += (f"🕗 Remaining days in the current month: {remaining_days}\n")
    daily_budget = remaining_budget / remaining_days
    summary += (f"👉 Budget Per Day: ${daily_budget:.2f}\n")

    return summary
