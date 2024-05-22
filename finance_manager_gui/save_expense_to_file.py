import sqlite3
from expense import Expense


#expense: an instance of the Expense class.
#expense_file_path: a string representing the file path to the SQLite database where the expense will be saved.
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"📍 Saving User Expense: {expense} to SQLite database")
    conn = sqlite3.connect(expense_file_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (name TEXT, amount REAL, category TEXT, date TEXT)''')
    c.execute("INSERT INTO expenses VALUES (?, ?, ?, ?)",
              (expense.name, expense.amount, expense.category, expense.date))
    conn.commit()
    conn.close()
