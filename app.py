from flask import Flask,render_template,redirect,url_for,request,session,flash,jsonify
from db import get_connection

app = Flask(__name__)

app.secret_key ='suhail_key'

@app.route('/')
def home():
      return render_template('home.html')

from flask import request, render_template

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users(name, email, password) VALUES(%s,%s,%s)",
            (name, email, password)
        )

        conn.commit()
        conn.close()
        flash("Signup successful! Please login.", "success")
        return redirect(url_for('home'))

    return render_template('signup.html')
      
@app.route('/login',methods=['GET','POST'])
def login():
      if request.method == 'POST':
            
            email = request.form['email']
            password = request.form['password']
            
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE email = %s and password = %s',(email,password))
            data = cursor.fetchone()
            conn.commit()
            conn.close()
            if data:
                  return render_template('home.html',data=data)
            else:
                 return render_template('login.html', error="Invalid credentials") 
      return render_template('login.html')
      
if __name__ =='__main__':
      app.run(debug=True)
            
