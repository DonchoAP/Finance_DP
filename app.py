<<<<<<< HEAD
import pandas as pd
from flask import Flask, render_template, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import matplotlib.pyplot as plt
import io
import xlsxwriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
import locale

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/financeapp'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class FinancialTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'income' or 'expense'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/add_transaction', methods=['POST'])
@login_required
def add_transaction():
    data = request.json
    new_transaction = FinancialTransaction(
        date=datetime.strptime(data['date'], '%Y-%m-%d'),
        amount=float(data['amount']),
        category=data['category'],
        department=data['department'],
        type=data['type']
    )
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/get_financial_data')
@login_required
def get_financial_data():
    transactions = FinancialTransaction.query.all()
    df = pd.DataFrame([(t.date, t.amount, t.category, t.department, t.type) for t in transactions],
                      columns=['date', 'amount', 'category', 'department', 'type'])
    return df.to_json(orient='records')

@app.route('/generate_report', methods=['POST'])
@login_required
def generate_report():
    report_type = request.json['type']
    format = request.json['format']
    
    df = pd.read_json(get_financial_data())
    
    if report_type == 'monthly':
        df['date'] = pd.to_datetime(df['date'])
        report = df.groupby([df['date'].dt.strftime('%Y-%m'), 'type'])['amount'].sum().unstack()
    elif report_type == 'quarterly':
        df['date'] = pd.to_datetime(df['date'])
        report = df.groupby([df['date'].dt.to_period('Q'), 'type'])['amount'].sum().unstack()
    
    if format == 'pdf':
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.drawString(100, 750, f"{report_type.capitalize()} Financial Report")
        p.drawString(100, 730, str(report))
        p.showPage()
        p.save()
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, attachment_filename=f'{report_type}_report.pdf', mimetype='application/pdf')
    elif format == 'excel':
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            report.to_excel(writer, sheet_name='Report')
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, attachment_filename=f'{report_type}_report.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@app.route('/analyze_data')
@login_required
def analyze_data():
    df = pd.read_json(get_financial_data())
    df['date'] = pd.to_datetime(df['date'])
    
    # Expense trends
    expense_trend = df[df['type'] == 'expense'].groupby(df['date'].dt.strftime('%Y-%m'))['amount'].sum()
    
    # Profit margins
    income = df[df['type'] == 'income']['amount'].sum()
    expenses = df[df['type'] == 'expense']['amount'].sum()
    profit_margin = (income - expenses) / income * 100 if income > 0 else 0
    
    # Predictions (simple moving average)
    df['month'] = df['date'].dt.to_period('M')
    monthly_totals = df.groupby(['month', 'type'])['amount'].sum().unstack()
    predictions = monthly_totals.rolling(window=3).mean().iloc[-1]
    
    return jsonify({
        'expense_trend': expense_trend.to_dict(),
        'profit_margin': profit_margin,
        'predictions': predictions.to_dict()
    })

@app.route('/monthly_closing')
@login_required
def monthly_closing():
    # This is a simplified version. In a real-world scenario, you'd need to integrate
    # with actual bank APIs and accounting software.
    df = pd.read_json(get_financial_data())
    df['date'] = pd.to_datetime(df['date'])
    
    last_month = pd.Timestamp.now().to_period('M') - 1
    monthly_data = df[df['date'].dt.to_period('M') == last_month]
    
    total_income = monthly_data[monthly_data['type'] == 'income']['amount'].sum()
    total_expenses = monthly_data[monthly_data['type'] == 'expense']['amount'].sum()
    balance = total_income - total_expenses
    
    return jsonify({
        'month': str(last_month),
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance
    })

@app.route('/change_language')
@login_required
def change_language():
    lang = request.args.get('lang', 'en')
    if lang == 'de':
        locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
    else:
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
=======
import pandas as pd
from flask import Flask, render_template, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import matplotlib.pyplot as plt
import io
import xlsxwriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
import locale

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/financeapp'
app.config['SECRET_KEY'] = 'your_secret_key_here'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class FinancialTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(10), nullable=False)  # 'income' or 'expense'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/add_transaction', methods=['POST'])
@login_required
def add_transaction():
    data = request.json
    new_transaction = FinancialTransaction(
        date=datetime.strptime(data['date'], '%Y-%m-%d'),
        amount=float(data['amount']),
        category=data['category'],
        department=data['department'],
        type=data['type']
    )
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/get_financial_data')
@login_required
def get_financial_data():
    transactions = FinancialTransaction.query.all()
    df = pd.DataFrame([(t.date, t.amount, t.category, t.department, t.type) for t in transactions],
                      columns=['date', 'amount', 'category', 'department', 'type'])
    return df.to_json(orient='records')

@app.route('/generate_report', methods=['POST'])
@login_required
def generate_report():
    report_type = request.json['type']
    format = request.json['format']
    
    df = pd.read_json(get_financial_data())
    
    if report_type == 'monthly':
        df['date'] = pd.to_datetime(df['date'])
        report = df.groupby([df['date'].dt.strftime('%Y-%m'), 'type'])['amount'].sum().unstack()
    elif report_type == 'quarterly':
        df['date'] = pd.to_datetime(df['date'])
        report = df.groupby([df['date'].dt.to_period('Q'), 'type'])['amount'].sum().unstack()
    
    if format == 'pdf':
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.drawString(100, 750, f"{report_type.capitalize()} Financial Report")
        p.drawString(100, 730, str(report))
        p.showPage()
        p.save()
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, attachment_filename=f'{report_type}_report.pdf', mimetype='application/pdf')
    elif format == 'excel':
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            report.to_excel(writer, sheet_name='Report')
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, attachment_filename=f'{report_type}_report.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

@app.route('/analyze_data')
@login_required
def analyze_data():
    df = pd.read_json(get_financial_data())
    df['date'] = pd.to_datetime(df['date'])
    
    # Expense trends
    expense_trend = df[df['type'] == 'expense'].groupby(df['date'].dt.strftime('%Y-%m'))['amount'].sum()
    
    # Profit margins
    income = df[df['type'] == 'income']['amount'].sum()
    expenses = df[df['type'] == 'expense']['amount'].sum()
    profit_margin = (income - expenses) / income * 100 if income > 0 else 0
    
    # Predictions (simple moving average)
    df['month'] = df['date'].dt.to_period('M')
    monthly_totals = df.groupby(['month', 'type'])['amount'].sum().unstack()
    predictions = monthly_totals.rolling(window=3).mean().iloc[-1]
    
    return jsonify({
        'expense_trend': expense_trend.to_dict(),
        'profit_margin': profit_margin,
        'predictions': predictions.to_dict()
    })

@app.route('/monthly_closing')
@login_required
def monthly_closing():
    # This is a simplified version. In a real-world scenario, you'd need to integrate
    # with actual bank APIs and accounting software.
    df = pd.read_json(get_financial_data())
    df['date'] = pd.to_datetime(df['date'])
    
    last_month = pd.Timestamp.now().to_period('M') - 1
    monthly_data = df[df['date'].dt.to_period('M') == last_month]
    
    total_income = monthly_data[monthly_data['type'] == 'income']['amount'].sum()
    total_expenses = monthly_data[monthly_data['type'] == 'expense']['amount'].sum()
    balance = total_income - total_expenses
    
    return jsonify({
        'month': str(last_month),
        'total_income': total_income,
        'total_expenses': total_expenses,
        'balance': balance
    })

@app.route('/change_language')
@login_required
def change_language():
    lang = request.args.get('lang', 'en')
    if lang == 'de':
        locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
    else:
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 69ae552e20184609c2863a8576937c506af29c90
