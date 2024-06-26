from flask import Flask, redirect, render_template, request, session, url_for
from sqlalchemy import create_engine, text

app = Flask(__name__)

conn_str = "mysql://root:Dougnang1@localhost/exam_management"
engine = create_engine(conn_str, echo=True)
conn = engine.connect()

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/signupS.html', methods=["GET"])
def signupS():
    return render_template("signupS.html")

@app.route('/signupS.html', methods=["POST"])
def signupSGo():
    conn.execute(text("INSERT INTO Student (First_Name, Last_Name, Email, Password) VALUES (:First_Name, :Last_Name, :Email, :Password)"), request.form)
    conn.commit()
    return render_template("index.html")

@app.route('/signupT.html', methods=["GET"])
def signupT():
    return render_template("signupT.html")

@app.route('/signupT.html', methods=["POST"])
def signupTGo():
    conn.execute(text("INSERT INTO Teacher (First_Name, Last_Name, Email, Password) VALUES (:First_Name, :Last_Name, :Email, :Password)"), request.form)
    conn.commit()
    return render_template("index.html")

@app.route('/studentHome.html')
def student():
    query = text("SELECT First_Name FROM Student WHERE Student_ID = :studentid")
    name = conn.execute(query, {'studentid' : studentID}).fetchone()
    return render_template('studentHome.html', name=name[0])

@app.route('/teachHome.html')
def teacher():
    query = text("SELECT First_Name FROM Teacher WHERE Teacher_ID = :teachid")
    name = conn.execute(query, {'teachid' : teachID}).fetchone()
    return render_template('teachHome.html', name=name[0])

@app.route('/loginS.html', methods=["GET"])
def loginS():
    return render_template('loginS.html')

@app.route('/loginS.html', methods=["POST"])
def loginSGo():
    email = request.form['Email']
    password = request.form['Password']

    query = text("SELECT Student_ID FROM Student WHERE Email = :email AND Password = :password")
    user = conn.execute(query, {'email': email, 'password': password}).fetchone()
    if user:
        global studentID
        studentID = user[0]
        query = text("SELECT First_Name FROM Student WHERE Student_ID = :studentid")
        name = conn.execute(query, {'studentid' : studentID}).fetchone()
        return render_template('studentHome.html', name=name[0])
    else:
        return render_template('loginS.html')

@app.route('/loginT.html', methods=["GET"])
def loginT():
    return render_template('loginT.html')

@app.route('/loginT.html', methods=["POST"])
def loginTGo():
    email = request.form['Email']
    password = request.form['Password']

    query = text("SELECT Teacher_ID FROM teacher WHERE Email = :email AND Password = :password")
    user = conn.execute(query, {'email': email, 'password': password}).fetchone()
    if user:
        global teachID
        teachID = user[0]
        query = text("SELECT First_Name FROM Teacher WHERE Teacher_ID = :teachid")
        name = conn.execute(query, {'teachid' : teachID}).fetchone()
        return render_template('teachHome.html', name=name[0])
    else:
        return render_template('loginT.html')

@app.route('/createTest.html', methods=["GET"])
def createTest():
    return render_template('createTest.html')

@app.route('/createTest.html', methods=["POST"])
def createTestGo():
    data = request.form['TestName']

    query = text("INSERT INTO Test (Teacher_ID, Test_Name) VALUES (:Teacher_ID, :Test_Name);")

    conn.execute(query, {'Teacher_ID': teachID, 'Test_Name': data})
    conn.commit()

    query = text("SELECT Test_ID FROM Test WHERE Test_Name = :Test_Name;")
    global TestID
    TestID = conn.execute(query, {'Test_Name' : data}).fetchone()[0]

    Q1 = request.form['Q1']
    Q2 = request.form['Q2']
    Q3 = request.form['Q3']
    Q4 = request.form['Q4']
    Q5 = request.form['Q5']
    Q6 = request.form['Q6']
    Q7 = request.form['Q7']
    Q8 = request.form['Q8']
    Q9 = request.form['Q9']
    Q10 = request.form['Q10']

    query = text("INSERT INTO Questions (Test_ID, Question) VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q1})
    conn.commit()

    query = text("INSERT INTO Questions (Test_ID, Question) VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q2})
    conn.commit()

    query = text("INSERT INTO Questions (Test_ID, Question) VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q3})
    conn.commit()

    query = text("INSERT INTO Questions (Test_ID, Question) VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q4})
    conn.commit()

    query = text("INSERT INTO Questions (Test_ID, Question) VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q5})
    conn.commit()

    query = text("INSERT INTO Questions (Test_ID, Question) VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q6})
    conn.commit()

    query = text("INSERT INTO Questions (Test_ID, Question) VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q7})
    conn.commit()

    query = text("INSERT INTO Questions (Test_ID, Question) VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q8})
    conn.commit()

    query = text("INSERT INTO Questions (Test_ID, Question) VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q9})
    conn.commit()

    query = text("INSERT INTO Questions (Test_ID, Question) VALUES (:Test_ID, :Question_Text);")
    conn.execute(query, {'Test_ID' : TestID, 'Question_Text' : Q10})
    conn.commit()

    return render_template("teachHome.html")

@app.route('/accounts.html')
def accounts():
    query = text("SELECT Teacher_ID, First_Name, Last_Name, Email FROM teacher")
    teacher_data = conn.execute(query)
    query = text("SELECT Student_ID, First_Name, Last_Name, Email FROM Student")
    student_data = conn.execute(query)

    return render_template('accounts.html', teacher_data=teacher_data, student_data=student_data)

@app.route('/accountsS.html')
def accountsS():
    query = text("SELECT Student_ID, First_Name, Last_Name, Email FROM Student")
    student_data = conn.execute(query)

    return render_template('accountsS.html', student_data=student_data)

@app.route('/accountsT.html')
def accountsT():
    query = text("SELECT Teacher_ID, First_Name, Last_Name, Email FROM teacher")
    teacher_data = conn.execute(query)

    return render_template('accountsT.html', teacher_data=teacher_data)

@app.route('/tests')
def tests():
    query = text("SELECT Test_ID, Test_Name FROM Test")
    tests = conn.execute(query).fetchall()
    return render_template('tests.html', tests=tests)

@app.route('/test_questions/<test_id>')
def test_questions(test_id):
    query = text("SELECT Question FROM Questions WHERE Test_ID = :test_id")
    questions = conn.execute(query, {'test_id' : test_id}).fetchall()
    return render_template('test_questions.html', questions=questions, test_id=test_id)

@app.route('/submit_answers/<test_id>', methods=['POST'])
def submit_answers(test_id):
    student_id = studentID
    query = text("SELECT Question FROM Questions WHERE Test_ID = :test_id")
    questions = conn.execute(query, {'test_id' : test_id}).fetchall()
    for question in questions:
        answer = request.form[question]
        query = text("INSERT INTO Answers (Test_ID, Student_ID, Answer) VALUES (:test_id, :student_id, :answer)")
        conn.execute(query, {'test_id': test_id, 'student_id': student_id, 'answer': answer})
    return redirect(url_for('tests'))

@app.route('/StudentResults')
def student_test_results():
    student_id = studentID
    query = text("SELECT Test.Test_ID, Test.Test_Name, Tests_Taken.Marks FROM Test JOIN Tests_Taken ON Test.Test_ID = Tests_Taken.Test_ID WHERE Tests_Taken.Student_ID = :student_id")
    tests = conn.execute(query, {'student_id': student_id}).fetchall()
    results = []
    for test in tests:
        results.append({'test_id': test[0], 'test_name': test[1], 'marks': test[2]})
    return render_template('StudentResults.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)