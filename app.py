from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            qualification TEXT NOT NULL,
            percentage REAL NOT NULL,
            skills TEXT NOT NULL,
            interest TEXT NOT NULL,
            preferred_course TEXT NOT NULL,
            career_goal TEXT NOT NULL,
            school_sports_experience TEXT
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("profile.html")


@app.route("/profile", methods=["POST"])
def profile():
    name = request.form["name"]
    qualification = request.form["qualification"]
    percentage = request.form["percentage"]
    skills = request.form["skills"]
    interest = request.form["interest"]
    preferred_course = request.form["preferred_course"]
    career_goal = request.form["career_goal"]
    school_sports_experience = request.form.get(
        "school_sports_experience", ""
    )

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (
            name, qualification, percentage, skills,
            interest, preferred_course, career_goal,
            school_sports_experience
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name, qualification, float(percentage), skills,
        interest, preferred_course, career_goal,
        school_sports_experience
    ))

    conn.commit()
    conn.close()

    return """
        <h1>Student Profile Saved Successfully!</h1>
        <p>Your information has been saved.</p>
        <a href="/">Back to Profile Form</a>
    """


if __name__ == "__main__":
    create_database()
    app.run(debug=True)