class Atm:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []
        self.menu()

    def menu(self):
        user_input = int(input("enter 1 to check balance\n"
                               "enter 2 to withdraw\n"
                               "enter 3 to deposit\n"
                               "enter 4 to transfer\n"
                               "enter 5 to change pin\n"
                               "enter 6 to view transaction history\n"
                               "enter 7 to exit\n"))

        if user_input == 1:
            self.check_balance()

        elif user_input == 2:
            self.withdraw()

        elif user_input == 3:
            self.deposit()

        elif user_input == 4:
            self.transfer()

        elif user_input == 5:
            self.change_pin()

        elif user_input == 6:
            self.view_transaction_history()

        elif user_input == 7:
            print("Thanks for using our ATM")

    def check_balance(self):
        pin = int(input("Enter your pin to validate you: "))
        if self.pin == pin:
            print(f"Your balance is {self.balance}")
            self.menu()
        else:
            print("You have entered wrong pin, try again")
            self.menu()

    def withdraw(self):
        pin = int(input("Enter your pin: "))
        if self.pin == pin:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"${amount} withdrawn successfully")
                self.transaction_history.append(f"Withdrawal: ${amount}")
                self.menu()
            else:
                print("Insufficient balance to withdraw")
                self.menu()
        else:
            print("You have entered wrong pin")
            self.menu()

    def deposit(self):
        pin = int(input("Enter your pin: "))
        if self.pin == pin:
            amount = int(input("Enter the amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"Deposit of ${amount} successful.")
                self.transaction_history.append(f"Deposit: ${amount}")
                print(f"Current balance: ${self.balance}")
            else:
                print("Invalid deposit amount. Please enter a positive number.")
        else:
            print("You have entered wrong pin")
        self.menu()

    def transfer(self):
        pin = int(input("Enter your pin: "))
        if self.pin == pin:
            recipient_account = input("Enter recipient's account number: ")
            amount = int(input("Enter transfer amount: "))
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f"${amount} transferred to account {recipient_account} successfully.")
                self.transaction_history.append(f"Transfer to account {recipient_account}: ${amount}")
                self.menu()
            elif amount <= 0:
                print("Invalid transfer amount. Please enter a positive number.")
                self.menu()
            else:
                print("Insufficient balance to transfer")
                self.menu()
        else:
            print("You have entered wrong pin")
            self.menu()

    def change_pin(self):
        old_pin = int(input("Enter your old pin: "))
        if self.pin == old_pin:
            new_pin = int(input("Enter your new pin: "))
            self.pin = new_pin
            print("Your pin is changed successfully!!!")
            self.menu()
        else:
            print("You have entered wrong pin")
            self.menu()

    def view_transaction_history(self):
        pin = int(input("Enter your pin to view transaction history: "))
        if self.pin == pin:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
            self.menu()
        else:
            print("You have entered wrong pin, try again")
            self.menu()


obj1 = Atm(1234, 10000)
