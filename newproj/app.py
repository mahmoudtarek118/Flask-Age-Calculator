from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    name = request.form['name']
    dob = request.form['dob']
    dob_date = datetime.strptime(dob, '%Y-%m-%d')
    
    # Calculate age
    today = datetime.today()
    age_years = today.year - dob_date.year
    age_months = today.month - dob_date.month
    age_days = today.day - dob_date.day
    if age_days < 0:
        age_months -= 1
        age_days += 30
    if age_months < 0:
        age_years -= 1
        age_months += 12

    return render_template('result.html', name=name, years=age_years, months=age_months, days=age_days)

if __name__ == '__main__':
    app.run(debug=True)
