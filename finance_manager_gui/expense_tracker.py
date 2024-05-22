import sqlite3
from get_user_expense import get_user_expense
from save_expense_to_file import save_expense_to_file
from summarize_expenses import summarize_expenses


def main():
    '''

   Takes the input for budget and saves it to the database
    '''
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.db"  # Change to SQLite database
    budget = int(input("Enter your budget: "))

    # Get user input for expense
    expense = get_user_expense()

    # Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    # Read file and summarize expense
    summarize_expenses(expense_file_path, budget)
