from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12M00h02o9mH%@127.0.0.1:3306/Training'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/pizza')
def pizza():
    pizzaToppings = ['Pepperoni', 'Cheese', 'Mushrooms', 'Sausage', 'Onions']
    return render_template('user.html', pizzaToppings=pizzaToppings, name='Pizza')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


