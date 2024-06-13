from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    name = request.form['name']
    dob = request.form['dob']
    dob = datetime.strptime(dob, '%Y-%m-%d')
    today = datetime.today()
    delta = today - dob
    age_years = delta.days // 365
    age_months = (delta.days % 365) // 30
    age_days = (delta.days % 365) % 30
    age_hours = delta.seconds // 3600
    age_minutes = (delta.seconds % 3600) // 60
    age_seconds = delta.seconds % 60
    return render_template('index.html', name=name, age_years=age_years,
                           age_months=age_months, age_days=age_days, 
                           age_hours=age_hours, age_minutes=age_minutes, 
                           age_seconds=age_seconds)

if __name__ == '__main__':
    app.run(debug=True)
