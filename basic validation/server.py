from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('validation.html')
@app.route('/process', methods=['Post'])
def process():
  if len(request.form['name'])<1:
      flash("Name cannot be empty")
  else:
      flash(f"success! your name is {request.form['name']}.")
      
      

  return redirect('/')

if __name__=="__main__":
    app.run(debug=True)