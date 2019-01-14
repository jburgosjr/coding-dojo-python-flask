from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "doesitevenneedone"

@app.route('/')
def index():
    return render_template("survey.html")

@app.route("/result", methods=["POST"])
def result():
    if len(request.form["name"])<1:
        flash("Name field can not be empty")
        return redirect("/")
    if len(request.form["comments"])<1:
        flash("Comment Field can not be empty")
        return redirect("/")
    if len(request.form["comments"])>120:
        flash("comment needs to be less than 120 characters")
        return redirect("/")
    else:
        name = request.form["name"]
        dojo_location = request.form["dojo_location"]
        favlanguage = request.form["favlanguage"]
        comments = request.form["comments"]
        return render_template("result.html", name = name, dojo_location = dojo_location, favlanguage = favlanguage, comments = comments)

    


@app.route("/danger")
def danger_back():
    print("a user tried to visit '/danger'.  we have redirected the user to '/'")
    return redirect("/")

    


    
   
if __name__=="__main__":
    
    app.run(debug=True) 