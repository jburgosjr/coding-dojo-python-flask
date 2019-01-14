from flask import Flask, render_template, redirect, request, session, flash
import re
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "giffemailplz"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def home():
    if 'id' not in session:
        session['id'] = False
    return render_template('email_validate.html')

@app.route('/validate', methods=['POST'])
def validate():
    error = False
    session['id']= request.form['email']
    mysql = connectToMySQL('email validation')
    query = "SELECT email FROM table1 WHERE email = %(verify_email)s;"
    data = {
        'verify_email':request.form['email']
    }
    compare = mysql.query_db(query,data)
    print(compare)

    

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email input format is Invalid")
        error = True

    if len(compare) > 0:
        flash("Email already stored")
        error = True
   
    if error == True:
        return redirect('/')

    elif error == False:
        mysql = connectToMySQL('email validation')
        query = "INSERT INTO table1 (email, created_at, updated_at) VALUES (%(Email)s, NOW(), NOW());"
        data = {
            'Email':request.form['email']
        }
        mysql.query_db(query,data)
        return redirect("/email_edit")

@app.route('/email_edit')
def admin():
    mysql = connectToMySQL('email validation')
    emails= mysql.query_db("SELECT * FROM table1")
    valid_email = session['id']
    
    return render_template('email_edit.html', emails=emails, valid_email=valid_email)

@app.route('/delete_email/<email_id>')
def delete_email(email_id):
    mysql= connectToMySQL('email validation')
    query = "DELETE FROM table1 where id = %(email_id)s;"
    data = {
        "email_id":email_id
    }
    mysql.query_db(query,data)
    return redirect('/email_edit')



   
    

    



    


if __name__=="__main__":
    app.run(debug=True)



