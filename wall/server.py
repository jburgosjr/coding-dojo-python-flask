from flask import Flask, render_template, redirect, request, session, flash, jsonify
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from time import strftime, localtime

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "itslogintime"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

@app.route('/')
def home():
    if 'id' not in session:
        session['id'] = 0
    if 'first_name' not in session:
        session['first_name'] = None
    if 'login_status' not in session:
        session['login_status'] = False
    if 'sent_msg_cnt' not in session:
        session['sent_msg_cnt'] = 0
   

    return render_template('logreg.html')

@app.route('/register_validate', methods=['POST'])
def validation():
    error=False
    mysql = connectToMySQL('dojo_wall')
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
        mysql = connectToMySQL('dojo_wall')
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
    mysql = connectToMySQL('dojo_wall')
    query = "SELECT * FROM users WHERE email = %(e_mail)s "
    data = {
        "e_mail":request.form['email']
    }
    check = mysql.query_db(query,data)
   
  
    if check:

        if check[0]['email'] == request.form['email']:
            if bcrypt.check_password_hash(check[0]['password'], request.form['password']):
                session['login_status'] = True
                session['first_name'] = check[0]['first_name']
                session['id'] = check[0]['id']
                return redirect('/home')
            else:
                flash ('Invalid Credentials: Login denied', 'login_top')
                return redirect('/')
    else:
        flash ('Invalid Credentials: Login denied', 'login_top')
        return redirect('/')

@app.route('/home')
def home_index():
    
    if session['login_status'] == True :
        time = strftime('%Y-%m-%d %H:%M:%S', localtime())
        mysql = connectToMySQL('dojo_wall')
        query = "SELECT messages.id, messages.user_id, messages.sent_to_id, messages.message, messages.created_at, messages.updated_at, users.first_name, users.last_name FROM messages join users on users.id = messages.user_id  WHERE messages.sent_to_id = %(user_id)s ORDER BY messages.created_at desc;"
        data = {
            'user_id':session['id']
        }
        message_check = mysql.query_db(query,data)
        count = 0
        for i in message_check:
            count+=1
        mysql2 = connectToMySQL('dojo_wall')
        send_query = "SELECT * FROM users WHERE NOT id = %(user_id)s;"
        send_data ={
            'user_id':session['id']
        }
        send_check = mysql2.query_db(send_query,send_data)
        return render_template('wall.html', messages = message_check, time=time, count = count, sends = send_check)
    else:
        return redirect('/')



@app.route('/logout')
def logout():

    session.clear()
    return redirect('/')

@app.route('/delete_message/<message_id>')
def del_msg(message_id):
    mysql = connectToMySQL('dojo_wall')
    query = 'select * from messages where id = %(message_id)s;'
    data = {
        'message_id':message_id
    }
    check = mysql.query_db(query,data)
    if check[0]['sent_to_id'] != session['id']:
        return redirect('/danger')
    elif check[0]['sent_to_id'] == session['id']:
        mysql = connectToMySQL('dojo_wall')
        query = "DELETE FROM messages where id = %(message)s"
        data = {
            'message':message_id
        }
        mysql.query_db(query,data)
        return redirect('/home')

@app.route('/send_message', methods = ['POST'])
def send_msg():
    mysql = connectToMySQL('dojo_wall')
    query = "SELECT * FROM users WHERE id = %(id)s "
    data = {
        "id":request.form['button']
    }
    users = mysql.query_db(query,data) 

    if len(request.form['message'])>250:
        flash("Message is over 250 characters. length of message is: %s"%(len(request.form['message'])), 'send_error')
        return redirect('/home')
    if len(request.form['message']) == 0:
        flash("Can not send an empty message. Write Something, dont be weird.", 'send_error')
        return redirect('/home')
    else:
        mysql = connectToMySQL('dojo_wall')
        query = "INSERT INTO messages (user_id, sent_to_id, message, created_at, updated_at) VALUES (%(user_id)s, %(sent_to_id)s, %(message)s, NOW(), NOW());"
        data = {
            "user_id":session['id'],
            "sent_to_id":request.form['button'],
            "message":request.form['message']
        }
        mysql.query_db(query,data)
        flash("Your message to %s %s has been sent" %(users[0]['first_name'], users[0]['last_name']), 'msg_success')
        session['sent_msg_cnt'] += 1
        return redirect('/home')

@app.route('/danger', methods=['GET'])
def danger():
    session['login_status'] = False
    return render_template('danger.html')
   

if __name__=="__main__":
    app.run(debug=True)


     # count = 1
        # time_since={}
        # for i in message_check:
            
        #     message_datetime = i['created_at']
        #     mysql = connectToMySQL('dojo_wall')
        #     query = "select timediff(%(current_datetime)s, %(message_datetime)s) as '';"
        #     data ={
        #         'current_datetime':strftime('%Y-%m-%d %H:%M:%S', localtime()),
        #         'message_datetime':message_datetime,
        #     }
        #     time_since['message_%s'%(count)] = mysql.query_db(query,data)
        #     count += 1

        # print(time_since)