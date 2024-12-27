from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

app.secret_key = 'your_secret_key'

# In-memory storage for registered users
registered_users = {}
levels_data = {
    "level1": {
        "available": ["Introduction to Python", "Web Development Essentials", "Computer Organization and Architecture"],
        "unavailable": ["Data Science Fundamentals", "Cybersecurity Basics", "Mathematics for Computer Science"],
    },
    "level2": {
        "available": ["Introduction to Computer Science", "Operating System", "Database 1"],
        "unavailable": ["Database 2", "Advanced Operating Systems", "Software Testing"],
    },
    "level3": {
        "available": ["Software Engineering", "Fundamental Programming 2", "Principles of Programming"],
        "unavailable": ["Mobile Application Development", "Distributed Systems", "Compiler Design"],
    },
    "level4": {
        "available": ["Machine Learning", "Networking", "Artificial Intelligence"],
        "unavailable": ["Deep Learning", "Big Data Analytics", "Blockchain Basics"],
    }
}

subjests = {
    1: {
        "title": "Introduction to Python",
        "description": "Learn Python programming from basics to advanced topics.",
        "instructor": "Omar Ehab",
        "duration": "18 weeks"
    },
    2: {
        "title": "Web Development Essentials",
        "description": "HTML, CSS, and JavaScript for building responsive websites.",
        "instructor": "DR. Shreif El-Shafeey",
        "duration": "18 weeks"
    },
    3: {
        "title": "Data Science Bootcamp",
        "description": "Master data analysis and machine learning with hands-on projects.",
        "instructor": "Hazem Shehab",
        "duration": "18 weeks"
    },
    4: {
        "title": "Computer Organization & Archticture",
        "description": "Studies how computer hardware and systems are designed and operate.",
        "instructor": "Jana Abd-El-Aziz",
        "duration": "18 weeks"
    },
    5: {
        "title": "Introduction To Computer Science",
        "description": "explores the basics of computing, programming, and algorithms.",
        "instructor": "Mohmed Reda",
        "duration": "18 weeks"
    },
    6: {
        "title": "Opreating System",
        "description": "covers concepts like process management, memory management, file systems, and system security.",
        "instructor": "Omier Sameh",
        "duration": "18 weeks"
    },
    7: {
        "title": "Software Enginering",
        "description": "focuses on designing, developing, testing, and maintaining reliable and efficient software systems.",
        "instructor": "Abd-El-Rhman Mohamed",
        "duration": "18 weeks"
    },
    8: {
        "title": "Database I",
        "description": "introduces database design, SQL, data modeling, and fundamentals of database management systems.",
        "instructor": "DR. Shady Mohmed",
        "duration": "18 weeks"
    },
    9: {
        "title": "Machine Learning",
        "description": "covers algorithms and techniques for enabling systems to learn and make predictions from data.",
        "instructor": "Ahmed Karem",
        "duration": "18 weeks"
    },
    10: {
        "title": "Princples Of Programming",
        "description": "introduces core concepts of programming languages, problem-solving, and algorithm development.",
        "instructor": "Ahmed Hamdy",
        "duration": "18 weeks"
    },
    11: {
        "title": "Fundmental Of Programming I",
        "description": "course covers basic programming concepts, including variables, control structures, functions, and simple algorithms.",
        "instructor": "Mayar Mohmed",
        "duration": "18 weeks"
    },
    12: {
        "title": "Algorithms",
        "description": "focuses on the design, analysis, and optimization of algorithms for solving computational problems efficiently.",
        "instructor": "DR. Ali Hamza",
        "duration": "18 weeks"
    },
    13: {
        "title": "Fundmental Of Programming II",
        "description": " builds on basic programming concepts, covering advanced topics like data structures, object-oriented programming, and algorithm design.",
        "instructor": "DR. Ahmed Saif",
        "duration": "18 weeks"
    },
}

qa_data = [
    {'question': 'What should I do if I forget my password?', 'answer': 'Click on the "Forgot Password" link on the login page and follow the instructions to reset your password.'},
    {'question': ' Where can I view my completed courses?', 'answer': 'Go to your "Dashboard" or "Profile" page. There’s a section called "Completed Courses" that lists all the courses you have finished.'},
    {'question': ' How do I contact my instructor?', 'answer': 'On the course page, there’s a "Contact Instructor" button. Click it to send a message directly to your instructor'},
    {'question': ' Is there a way to interact with other students?', 'answer': 'Yes, you can interact with other students through the discussion forums, group activities, or chat features available in the LMS.'},
]

users = [
    {"id": 42210220, "name": "Omar Ehab", "join_date": "2022-01-15", "courses": []},
    {"id": 42210021, "name": "Omier Sameh", "join_date": "2022-02-10", "courses": []},
    {"id": 42210207, "name": "Ahmed Nasr", "join_date": "2022-03-22", "courses": []},
    {"id": 42210286, "name": "Jana Abdelaziz", "join_date": "2022-02-10", "courses": []},
    {"id": 42210018, "name": "Hazem Shehab", "join_date": "2022-02-10", "courses": []},
    {"id": 42210267, "name": "Abdelrahman Mohamed", "join_date": "2022-02-10", "courses": []},
    {"id": 42210228, "name": "Mohmed Sorour", "join_date": "2022-02-10", "courses": []}

]

courses = [
    {"id": "101", "name": "Python Basics"},
    {"id": "102", "name": "Data Science 101"},
    {"id": "103", "name": "Web Development"}
]




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/courses")
def course():
    return render_template('course.html', levels=levels_data)

@app.route("/details")
def details():
    return render_template("details.html" , courses=subjests)  # Course details page

@app.route("/sign")
def index():
    return render_template("login.html")  # Register/Login page
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Check if the user is registered
    if email in registered_users and registered_users[email] == password:
        flash('Login successful', 'success')
        return redirect(url_for('dashboard'))  # Redirect to the dashboard page
    else:
        flash('Invalid credentials, please try again', 'danger')
        return redirect(url_for('index'))


@app.route('/register', methods=['POST'])
def register():
    # Handle registration logic here
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # Check if the email is already registered
    if email in registered_users:
        flash('Email already registered', 'danger')
    else:
        # Add the new user to the in-memory storage
        registered_users[email] = password
        flash('Registration successful!', 'success')
    
    return redirect(url_for('index'))

@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    # Handle forgot password logic here
    email = request.form['email']
    flash('Check your email for password reset instructions', 'success')
    return redirect(url_for('index'))


@app.route('/feedjana', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        course = request.form['course']
        feedback = request.form['feedback']
        
        # Process the feedback (for now, print it to the console)
        print(f"Feedback received from {name} for {course}: {feedback}")

        # You can save feedback to a file or database here if needed

        # Show the success message
        return render_template('jana.html', message="Thank you for your feedback!")
    
    return render_template('jana.html')

@app.route('/feedback')
def faq():
    return render_template('feedback.html', qa_data=qa_data)



@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", users=users, courses=courses)

@app.route("/assign_course", methods=["POST"])
def assign_course():
    data = request.json
    user_id = int(data.get("user_id"))
    course_id = data.get("course_id")

    # Find user and course
    user = next((user for user in users if user["id"] == user_id), None)
    course = next((course for course in courses if course["id"] == course_id), None)

    if user and course:
        if course not in user["courses"]:
            user["courses"].append(course)
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "message": "Course already assigned"}), 400

    return jsonify({"success": False, "message": "Invalid user or course ID"}), 400
@app.route('/logout')
def logout():
    # يتم تسجيل الخروج وإعادة توجيه المستخدم إلى صفحة تسجيل الدخول
    flash('You have logged out', 'info')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)