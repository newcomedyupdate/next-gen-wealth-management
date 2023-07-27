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

# ... (remaining code)
