from flask import Flask, render_template, redirect, request, session, flash
import re
app = Flask(__name__)
app.secret_key = 'dontevenneedit'
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/validate", methods=["POST"])
def input_check():
    error=False
    
    if len(request.form["first_name"]) == 0 or len(request.form["last_name"]) == 0 or len(request.form["email"]) == 0 or len(request.form["password"]) == 0 or len(request.form["confirm_password"]) == 0:
        flash("All input fileds are required")
        error=True
    else:
        if not NAME_REGEX.match(request.form["first_name"]):
            flash("First Name field can not contain numbers")
            error=True

        if not NAME_REGEX.match(request.form["last_name"]):
            flash("Last Name field can not contain numbers")
            error=True

        if len(request.form["password"])< 8:
            flash("Password must be more than 8 characters")
            error=True
        
        if not EMAIL_REGEX.match(request.form["email"]):
            flash("Invalid Email format")
            error=True

        if request.form["password"] != request.form["confirm_password"]:
            flash("Passwords do not match")
            error=True

    

    if error == True:
        return redirect("/")




if __name__=="__main__":
    app.run(debug=True)