from flask import render_template, Flask, request
from mysite import cursor
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('page1.html',x='maria')

@app.route('/kostas')
def kostas():
    return render_template('page1.html',x='kostas')

@app.route('/convert')
def convert():
    return render_template('convert.html')

@app.route('/mathites')
def mathites():
    cursor.execute(
    ''' Select id,name,phone from mathites
    ''')

    records=cursor.fetchall()
    return render_template('mathites.html',rows=records)

@app.route('/result' , methods=["POST"])
def result():
    fahrenheit = int(request.form["fahrenheit"])
    celsius = (fahrenheit - 32) * 5.0/9.0
    return f"H thermokrasia einai {celsius}"
