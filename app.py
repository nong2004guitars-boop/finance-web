from flask import Flask, render_template_string
from collections import defaultdict

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>Financial Summary Statement</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f7f6; color: #333; }
        .container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { text-align: center; color: #2c3e50; }
        .summary { display: flex; justify-content: space-between; background: #eef2f3; padding: 15px; border-radius: 6px; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
        th { background-color: #f2f2f2; }
        .income { color: #27ae60; font-weight: bold; }
        .expense { color: #c0392b; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Financial Summary Statement</h1>
        
        <div class="summary">
            <div>
                <p>Total Income: <span class="income">${{ "{:,.2f}".format(total_income) }}</span></p>
                <p>Total Expenses: <span class="expense">${{ "{:,.2f}".format(total_expense) }}</span></p>
            </div>
            <div>
                <h3>Net Balance: ${{ "{:,.2f}".format(net_balance) }}</h3>
            </div>
        </div>

        <h3>Transaction History</h3>
        <table>
            <tr>
                <th>Date</th>
                <th>Type</th>
                <th>Category</th>
                <th>Amount</th>
            </tr>
            {% for item in transactions %}
            <tr>
                <td>{{ item.date }}</td>
                <td class="{{ 'income' if item.type == 'Income' else 'expense' }}">{{ item.type }}</td>
                <td>{{ item.category }}</td>
                <td>${{ "{:,.2f}".format(item.amount) }}</td>
            </tr>
            {% endfor %}
        </table>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    transactions = [
        {"date": "2026-09-15 09:00", "type": "Income", "category": "Salary", "amount": 3000.00},
        {"date": "2026-09-15 12:30", "type": "Expense", "category": "Lunch & Coffee", "amount": 15.50},
        {"date": "2026-09-16 18:00", "type": "Expense", "category": "Groceries", "amount": 85.20},
        {"date": "2026-09-18 14:00", "type": "Income", "category": "Freelance Work", "amount": 450.00},
        {"date": "2026-09-19 20:00", "type": "Expense", "category": "Electricity Bill", "amount": 120.00},
    ]

    total_income = sum(item["amount"] for item in transactions if item["type"] == "Income")
    total_expense = sum(item["amount"] for item in transactions if item["type"] == "Expense")
    net_balance = total_income - total_expense

    return render_template_string(HTML_TEMPLATE, 
                                  transactions=transactions,
                                  total_income=total_income,
                                  total_expense=total_expense,
                                  net_balance=net_balance)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
