from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "itslogintime"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def home():
    if 'id' not in session:
        session['id'] = False
    if 'first_name' not in session:
        session['first_name'] = None
   

    return render_template('login_register.html')

@app.route('/register_validate', methods=['POST'])
def validation():
    error=False
    mysql = connectToMySQL('login_register')
    query = "SELECT * FROM users WHERE email = %(e_mail)s "
    data = {
        "e_mail":request.form['email']
    }
    check = mysql.query_db(query,data)

    if len(request.form["first_name"]) == 0 or len(request.form["last_name"]) == 0 or len(request.form["email"]) == 0 or len(request.form["password"]) == 0 or len(request.form["confirm_password"]) == 0:
        flash("All input fileds are required", 'top')
        error=True
    else:
        if not NAME_REGEX.match(request.form["first_name"]):
            flash("First Name field can not contain numbers", 'frname')
            error=True
        
        if len(request.form['first_name'])<2:
            flash('Invalid name length: First Name', 'frname')

        if not NAME_REGEX.match(request.form["last_name"]):
            flash("Last Name field can not contain numbers", 'last_name')
            error=True

        if len(request.form['last_name'])<2:
            flash('Invalid name length: Last Name', 'last_name')

        if len(request.form["password"])< 8:
            flash("Password must be more than 8 characters", 'password')
            error=True

        if check:
            if check[0]['email'] == request.form['email']:
                flash("Email has already been registered", 'email')
                error=True

        if not EMAIL_REGEX.match(request.form["email"]):
            flash("Invalid Email format", 'email')
            error=True

        if request.form["password"] != request.form["confirm_password"]:
            flash("Passwords do not match", 'password')
            error=True

    if error == True:
        return redirect('/')
    elif error == False:
        reg_pass_hash = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL('login_register')
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(frname)s, %(lsname)s, %(e_mail)s, %(pass)s, NOW(), NOW());" 
        data = {
            "frname":request.form['first_name'],
            "lsname":request.form['last_name'],
            "e_mail":request.form['email'],
            'pass':reg_pass_hash
        }
        mysql.query_db(query,data)
        flash('Registration Successful! Thank you for registering, you may now log in', 'success')
        return redirect('/')

@app.route('/login_validate', methods=["POST"])
def login_val():
    mysql = connectToMySQL('login_register')
    query = "SELECT * FROM users WHERE email = %(e_mail)s "
    data = {
        "e_mail":request.form['email']
    }
    check = mysql.query_db(query,data)
   
  
    if check:

        if check[0]['email'] == request.form['email']:
            if bcrypt.check_password_hash(check[0]['password'], request.form['password']):
                session['id'] = True
                session['first_name'] = check[0]['first_name']
                return redirect('/home')
            else:
                flash ('Invalid Credentials: Login denied', 'login_top')
                return redirect('/')
    else:
        flash ('Invalid Credentials: Login denied', 'login_top')
        return redirect('/')

@app.route('/home')
def home_index():
    
    if session['id'] == True :
        return render_template('home.html')
    else:
        return redirect('/')

@app.route('/logout')
def logout():

    session.clear()
    return redirect('/')


        




      


   
    

    
if __name__=="__main__":
    app.run(debug=True)
