from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'dontevenneedit'

@app.route("/")
def index():
    mysql = connectToMySQL("lead_gen_business")
    clients = mysql.query_db("select concat(clients.first_name,' ',clients.last_name) as name, count(leads.leads_id) as leads from clients join sites on clients.client_id = sites.client_id join leads on sites.site_id = leads.site_id where clients.client_id < 5 group by clients.first_name order by clients.client_id ;")
    print ("fetched all clients",clients)
    return render_template("dashboard.html", clients=clients)



       
   



if __name__=="__main__":
    app.run(debug=True)