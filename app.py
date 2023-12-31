
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with your secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database for simplicity
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
        else:
            new_user = User(username=username, password_hash=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('dashboard'))
    return render_template('register.html')

# ... (previous code)

@app.route('/dashboard')
@login_required
def dashboard():
    # Get the user's risk profile (you can use a more advanced logic in a real application)
    # For simplicity, we'll use a predefined risk profile 'conservative' for users in this example.
    risk_profile = 'conservative'

    # Simple AI-based recommendation system (you can enhance this further)
    if risk_profile == 'conservative':
        investment_recommendation = 'Invest in low-risk bonds and blue-chip stocks.'
    elif risk_profile == 'moderate':
        investment_recommendation = 'Diversify your portfolio with a mix of stocks and bonds.'
    else:
        investment_recommendation = 'Consider higher-risk assets like growth stocks and mutual funds.'

    return render_template('dashboard.html', recommendation=investment_recommendation)

# ... (remaining code)


# ... (previous code)

@app.route('/budget', methods=['GET', 'POST'])
@login_required
def budget():
    if request.method == 'POST':
        income = float(request.form['income'])
        expenses = float(request.form['expenses'])
        savings = income - expenses

        return render_template('budget_result.html', income=income, expenses=expenses, savings=savings)

    return render_template('budget.html')

@app.route('/retirement', methods=['GET', 'POST'])
@login_required
def retirement():
    if request.method == 'POST':
        current_age = int(request.form['current_age'])
        retirement_age = int(request.form['retirement_age'])
        current_savings = float(request.form['current_savings'])
        annual_contributions = float(request.form['annual_contributions'])
        inflation_rate = float(request.form['inflation_rate'])
        investment_return = float(request.form['investment_return'])

        years_until_retirement = retirement_age - current_age
        future_value = current_savings * (1 + investment_return) ** years_until_retirement
        total_contributions = annual_contributions * years_until_retirement
        future_value += total_contributions

        return render_template('retirement_result.html', future_value=future_value)

    return render_template('retirement.html')

import random


@app.route('/dashboard')
@login_required
def dashboard():

    return 'Welcome to the Next-Gen Wealth Management Dashboard!'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

    # ... (previous code)
    # Sample asset allocation data (for demonstration purposes)
    asset_allocation = {
        'Stocks': 40,
        'Bonds': 30,
        'Cash': 20,
        'Real Estate': 10,
    }

    # Generate a simple bar chart for asset allocation using Matplotlib
    import matplotlib.pyplot as plt

    plt.bar(asset_allocation.keys(), asset_allocation.values())
    plt.xlabel('Asset Class')
    plt.ylabel('Percentage')
    plt.title('Portfolio Asset Allocation')
    plt.tight_layout()

    # Save the plot as a PNG file
    plt.savefig('static/portfolio_allocation.png')

    return render_template('dashboard.html', recommendation=investment_recommendation)

    # Generate mock real-time market data for demonstration (replace this with real data in a production app)
    stock_prices = {
        'AAPL': random.uniform(120, 140),
        'GOOG': random.uniform(2700, 2900),
        'AMZN': random.uniform(3500, 3700),
        'MSFT': random.uniform(270, 290),
        'TSLA': random.uniform(650, 700),
    }

    return render_template('dashboard.html', recommendation=investment_recommendation, stock_prices=stock_prices)

# ... (remaining code)

