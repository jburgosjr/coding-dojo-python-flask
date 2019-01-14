from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'dontevenneedit'

@app.route("/")
def index():
    mysql = connectToMySQL("friendsdb")
    friends = mysql.query_db("SELECT * FROM friends")
    print ("fetched all friends",friends)
    return render_template("index.html", friends=friends)

@app.route("/add_homie", methods=["POST"])
def insert():
    mysql = connectToMySQL("friendsdb")
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW())"
    data ={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "occupation":request.form["occupation"],
    }     

    mysql.query_db(query,data)
    return redirect("/")





if __name__=="__main__":
    app.run(debug=True)