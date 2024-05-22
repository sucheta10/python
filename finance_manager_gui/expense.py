from datetime import datetime #This line imports the datetime class from the datetime module, which is used for manipulating dates and times.

class Expense:
    def __init__(self, name, category, amount, date=None): #constructor for expense class
                                                           # name: the name of the expense (e.g., "Groceries").
                                                           # category: the category of the expense (e.g., "Food").
                                                           # amount: the amount of the expense (e.g., 50.00).
                                                           # date: the date of the expense, which is optional and defaults to None.
#This line assigns the value of the name parameter to the name attribute of the instance.
        self.name = name
# This line assigns the value of the category parameter to the category attribute of the instance.
        self.category = category
# This line assigns the value of the amount parameter to the amount attribute of the instance.
        self.amount = amount
# If date is None, it assigns the current date in the format "YYYY-MM-DD" to the date attribute. The datetime.now() method returns the current date and time, and strftime("%Y-%m-%d") formats it as a string in the "YYYY-MM-DD" format.
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def __repr__(self):  #special method used to provide a string representation of the object.
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}, {self.date}>"
