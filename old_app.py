"""
    updated implementation that displays each report on its own page with a menu
"""
    
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/all_faculty")
def all_faculty():
    # Connect to the database
    conn = sqlite3.connect("faculty_committees.db")
    c = conn.cursor()

    # Get all faculty
    c.execute("SELECT FacultyName FROM Faculty")
    all_faculty = c.fetchall()

    # Close the connection
    conn.close()

    return render_template("all_faculty.html", all_faculty=all_faculty)

@app.route("/all_committees")
def all_committees():
    # Connect to the database
    conn = sqlite3.connect("faculty_committees.db")
    c = conn.cursor()

    # Get all committees
    c.execute("SELECT CommitteeName, CommitteeCode FROM Committee")
    all_committees = c.fetchall()

    # Close the connection
    conn.close()

    return render_template("all_committees.html", all_committees=all_committees)

@app.route("/all_time_faculty_participation")
def all_time_faculty_participation():
    # Connect to the database
    conn = sqlite3.connect("faculty_committees.
