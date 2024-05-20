import sqlite3
import sys
import re
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTableWidget, QTableWidgetItem, QLineEdit, QFormLayout, QMessageBox
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtCore import QThread, pyqtSignal

# Database Setup
def create_db():
    conn = sqlite3.connect('personal_finance_manager.db')
    c = conn.cursor()

    c.execute('''
              CREATE TABLE IF NOT EXISTS budgets (
                  id INTEGER PRIMARY KEY,
                  category TEXT NOT NULL,
                  "limit" REAL NOT NULL
              )
          ''')

    c.execute('''
              CREATE TABLE IF NOT EXISTS transactions (
                  id INTEGER PRIMARY KEY,
                  date TEXT,
                  description TEXT,
                  category TEXT,
                  amount REAL
              )
          ''')

    conn.commit()
    conn.close()

create_db()

# GUI with PyQt5
class FinanceManager(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Personal Finance Manager')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.upload_btn = QPushButton('Import Transactions')
        self.upload_btn.clicked.connect(self.import_transactions)

        self.budget_btn = QPushButton('Set Budget')
        self.budget_btn.clicked.connect(self.set_budget)

        self.visualize_btn = QPushButton('Visualize Data')
        self.visualize_btn.clicked.connect(lambda: [self.visualize_data(), self.check_budget(), self.show_monthly_summary()])

        self.update_rates_btn = QPushButton('Update Exchange Rates')
        self.update_rates_btn.clicked.connect(self.update_exchange_rates)

        self.layout.addWidget(self.upload_btn)
        self.layout.addWidget(self.budget_btn)
        self.layout.addWidget(self.visualize_btn)
        self.layout.addWidget(self.update_rates_btn)

        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.central_widget.setLayout(self.layout)

        self.exchange_rates = {}

    def import_transactions(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_name:
            self.import_thread = ImportThread(file_name)
            self.import_thread.finished.connect(lambda: QMessageBox.information(self, "Success", "Transactions imported successfully."))
            self.import_thread.start()

    def update_table(self, df):
        self.table_widget.setRowCount(len(df))
        self.table_widget.setColumnCount(len(df.columns))
        self.table_widget.setHorizontalHeaderLabels(df.columns)

        for i, row in df.iterrows():
            for j, col in enumerate(df.columns):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(row[col])))

        self.table_widget.resizeColumnsToContents()

    def set_budget(self):
        self.budget_window = QWidget()
        self.budget_window.setWindowTitle('Set Budget')
        self.budget_window.setGeometry(200, 200, 300, 200)

        layout = QFormLayout()

        self.category_input = QLineEdit()
        self.limit_input = QLineEdit()
        self.currency_input = QLineEdit()

        layout.addRow('Category:', self.category_input)
        layout.addRow('Limit:', self.limit_input)
        layout.addRow('Currency:', self.currency_input)

        save_btn = QPushButton('Save Budget')
        save_btn.clicked.connect(self.save_budget)
        layout.addWidget(save_btn)

        self.budget_window.setLayout(layout)
        self.budget_window.show()

    def save_budget(self):
        category = self.category_input.text()
        limit = float(self.limit_input.text())
        currency = self.currency_input.text().upper()

        # Ensure exchange rates are updated
        if currency != 'USD' and currency not in self.exchange_rates:
            self.update_exchange_rates()

        if currency != 'USD':
            converted_limit = self.convert_currency(limit, currency, 'USD')
        else:
            converted_limit = limit

        conn = sqlite3.connect('personal_finance_manager.db')
        c = conn.cursor()
        try:
            c.execute('INSERT INTO budgets (category, "limit") VALUES (?, ?)', (category, converted_limit))
            conn.commit()
            QMessageBox.information(self, "Success", "Budget set successfully.")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error inserting into database: {e}")
        finally:
            conn.close()

        self.budget_window.close()

    def visualize_data(self):
        conn = sqlite3.connect('personal_finance_manager.db')
        df = pd.read_sql_query('SELECT * FROM transactions', conn)
        conn.close()

        category_summary = df.groupby('category')['amount'].sum().reset_index()

        plt.figure(figsize=(10, 5))
        plt.bar(category_summary['category'], category_summary['amount'], color='skyblue')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Spending by Category')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def check_budget(self):
        conn = sqlite3.connect('personal_finance_manager.db')
        transactions_df = pd.read_sql_query('SELECT * FROM transactions', conn)
        budgets_df = pd.read_sql_query('SELECT * FROM budgets', conn)
        conn.close()

        category_spending = transactions_df.groupby('category')['amount'].sum().reset_index()

        for _, row in budgets_df.iterrows():
            category = row['category']
            limit = row['limit']

            spending = category_spending[category_spending['category'] == category]['amount'].sum()

            if spending >= limit:
                QMessageBox.warning(self, "Budget Exceeded", f"You have exceeded the budget for {category}.")
            elif spending >= 0.9 * limit:
                QMessageBox.warning(self, "Budget Alert", f"You are approaching the budget limit for {category}.")

    def show_monthly_summary(self):
        conn = sqlite3.connect('personal_finance_manager.db')
        df = pd.read_sql_query('SELECT * FROM transactions', conn)
        conn.close()

        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M')

        monthly_summary = df.groupby('month')['amount'].sum().reset_index()
        monthly_summary['savings'] = 1000 - monthly_summary['amount']  # Assuming a fixed income of 1000 for simplicity

        self.table_widget.setRowCount(len(monthly_summary))
        self.table_widget.setColumnCount(len(monthly_summary.columns))
        self.table_widget.setHorizontalHeaderLabels(monthly_summary.columns)

        for i, row in monthly_summary.iterrows():
            for j, col in enumerate(monthly_summary.columns):
                self.table_widget.setItem(i, j, QTableWidgetItem(str(row[col])))

        self.table_widget.resizeColumnsToContents()

    def update_exchange_rates(self):
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        response = requests.get(url)
        data = response.json()

        self.exchange_rates = data['rates']
        QMessageBox.information(self, "Success", "Exchange rates updated successfully.")

    def convert_currency(self, amount, from_currency, to_currency):
        # Update exchange rates if not already updated
        if not self.exchange_rates:
            self.update_exchange_rates()

        # Check if from_currency is USD
        if from_currency == 'USD':
            if to_currency not in self.exchange_rates:
                raise ValueError(f"Currency '{to_currency}' not found in exchange rates.")
            converted_amount = amount * self.exchange_rates[to_currency]
        else:
            if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
                raise ValueError(f"Currency '{from_currency}' or '{to_currency}' not found in exchange rates.")

            amount_in_usd = amount / self.exchange_rates[from_currency]
            converted_amount = amount_in_usd * self.exchange_rates[to_currency]

        return converted_amount

    def categorize_transaction(descriptions):
        categories = {
            'groceries': ['supermarket', 'grocery'],
            'utilities': ['electricity', 'water', 'gas'],
            'entertainment': ['cinema', 'movie', 'theater'],
            'dining': ['restaurant', 'cafe', 'dining']
        }

        results = []
        for description in descriptions:
            matched_category = 'other'  # Default category if no match is found
            for category, keywords in categories.items():
                for keyword in keywords:
                    if re.search(keyword, str(description), re.IGNORECASE):
                        matched_category = category
                        break
            results.append(matched_category)
        return results

    def create_db(self):
        conn = sqlite3.connect('personal_finance_manager.db')
        c = conn.cursor()

        c.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                date TEXT,
                description TEXT,
                category TEXT,
                amount REAL
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY,
                category TEXT,
                limit REAL
            )
        ''')

        conn.commit()
        conn.close()


class ImportThread(QThread):
    finished = pyqtSignal()

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def run(self):
        df = pd.read_csv(self.file_name)

        # Ensure 'description' column exists in the DataFrame
        if 'description' in df.columns:
            df['category'] = FinanceManager.categorize_transaction(df['description'])
        else:
            QMessageBox.warning(None, "Warning", "The 'description' column does not exist in the CSV file.")
            return

        conn = sqlite3.connect('personal_finance_manager.db')
        df.to_sql('transactions', conn, if_exists='append', index=False)
        conn.close()

        self.finished.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FinanceManager()
    window.show()
    sys.exit(app.exec_())
