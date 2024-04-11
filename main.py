from flask import Flask, render_template, request
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
    return render_template('studentHome.html')

@app.route('/teachHome.html')
def teacher():
    return render_template('teachHome.html')

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
        return render_template('studentHome.html')
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
        return render_template('teachHome.html')
    else:
        return render_template('loginT.html')

if __name__ == '__main__':
    app.run(debug=True)