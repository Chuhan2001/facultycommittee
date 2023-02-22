"""
Write a Python Flask application that has separate pages to display all faculty, all committees, faculty participation in committee for all time sorted by academic year, and faculty participation in committee for last 5 academic years sorted by year. App must have a menu. Use this database schema: 
Committee (Designation, Committee Code, Committee Name, Committee Type)
Faculty (Faculty Email, Faculty Name)
Faculty-Committee(Committee Code, Faculty Name, Faculty Start Semester, Membership Type, Designation, Academic Year) 
"""
from flask import Flask, render_template
# pip3 install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

app = Flask(__name__)

# Configure the application with a database
# to create a new database run this command in terminal:
# sqlite faculty_committees.db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///faculty_committees.db'
db = SQLAlchemy(app)

# Define the models
class Faculty(db.Model):
    faculty_email = db.Column(db.String(255), primary_key=True)
    faculty_name = db.Column(db.String(255), unique=True, nullable=False)

class Committee(db.Model):
    designation = db.Column(db.String(255))
    committee_code = db.Column(db.String(255), primary_key=True )
    committee_name = db.Column(db.String(255), unique=True, nullable=False)
    committee_type = db.Column(db.String(255))

class Faculty_Committee(db.Model):
    committee_code = db.Column(db.String(255), ForeignKey("committee.committee_code"), primary_key=True, nullable=False)
    faculty_email = db.Column(db.String(255), ForeignKey("faculty.faculty.email"), primary_key=True, nullable=False)
    faculty_end_semester = db.Column(db.String(255))
    membership_type = db.Column(db.String(255))
    designation = db.Column(db.String(255))
    academic_year = db.Column(db.String(255), primary_key=True, nullable=False)

# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/faculty')
def faculty():
    faculty_list = Faculty.query.all()
    return render_template('faculty.html', faculty_list=faculty_list)
    #return render_template('faculty.html')

@app.route('/committees')
def committees():
    committee_list = Committee.query.all()
    return render_template('committees.html', committee_list=committee_list)

@app.route('/faculty-committee-all')
def faculty_committee_all():
    faculty_committee_list = Faculty_Committee.query.order_by(Faculty_Committee.academic_year).all()
    return render_template('faculty_committee_all.html', faculty_committee_list=faculty_committee_list)

@app.route('/faculty-committee-last-five')
def faculty_committee_last_five():
    faculty_committee_list = Faculty_Committee.query.order_by(Faculty_Committee.academic_year.desc()).limit(5).all()
    return render_template('faculty_committee_last_five.html', faculty_committee_list=faculty_committee_list)

if __name__ == '__main__':
    app.run(debug=True)