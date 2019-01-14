from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def initial_render():
    return render_template("test.html")
    

@app.route("/table")
def fill_table():
  users = (
   {'first_name' : 'Michael', 'last_name' : 'Choi', 'entry_number': '1'},
   {'first_name' : 'John', 'last_name' : 'Supsupin', 'entry_number': '2'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen', 'entry_number': '3'},
   {'first_name' : 'KB', 'last_name' : 'Tonel', 'entry_number': '4'}
  )

  return render_template("htmltable.html", users = users)


  


if __name__ == "__main__":
    app.run(debug = True)
