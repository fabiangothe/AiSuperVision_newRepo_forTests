
#added myself
import pymysql
pymysql.install_as_MySQLdb()
#------

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:AbCd123!@localhost/documentation_test_database'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
'''
class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100), doc="test_Doc")
    city = db.Column(db.String(50), doc="test_Doc")
    addr = db.Column(db.String(200), doc="test_Doc")
    pin = db.Column(db.String(10), doc="test_Doc")
'''
#'''
from sqlalchemy import MetaData
metadata_obj = MetaData()

for t in metadata_obj.sorted_tables:
    print(t.name)
#'''

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, doc="Documentation for id")
    name = db.Column(db.String(50), nullable=False, doc="Documentation for name")
    addresses = db.relationship('Address', backref='person', lazy=True, doc="Documentation for addresses")

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, doc="Documentation for id")
    email = db.Column(db.String(120), nullable=False, doc="Documentation for email")
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
                          nullable=False, doc="Documentation for person_id")

'''
def __init__(self, name, city, addr,pin):
    self.name = name
    self.city = city
    self.addr = addr
    self.pin = pin

'''
'''
@app.route('/')
def show_all():
    return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'], request.form['city'],
                               request.form['addr'], request.form['pin'])

            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')
'''

#'''
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
#'''