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

@app.route('/studentHome.html')
def student():
    return render_template('studentHome.html')

@app.route('/teachHome.html')
def teacher():
    return render_template('teachHome.html')

if __name__ == '__main__':
    app.run(debug=True)