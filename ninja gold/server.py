from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "gimmedaloot"


@app.route("/")
def start():

    if "gold_count" not in session:
        session["gold_count"] = 0

    if "act_log" not in session:
        print("We ain't found shit")
        session["act_log"] = []

    
    act_log = session["act_log"]

    gold_count = session["gold_count"]

    return render_template("ninja_gold.html", act_log = act_log, gold_count = gold_count)

@app.route("/process_money", methods=["POST"])
def get_gold():
    
    if request.form["button"] == "farm":
        no_whammies = random.randrange(1,3)
        if no_whammies == 1:
            goldval = random.randrange(1,9)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='greentext'>Got yourself a good crop this season. you've earned %s gold  (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session.modified = True
            session["gold_count"] += goldval
        if no_whammies == 2:
            goldval = random.randrange(1,9)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> Farming aint what it used to be. your crop is trash. you loose %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval

    
    if request.form["button"] == "cave":
        no_whammies = random.randrange(1,3)
        if no_whammies == 1:
            goldval = random.randrange(0,11)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='greentext'> Youve found some treasure! Found %s gold!  (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] += goldval
        if no_whammies == 2:
            goldval = random.randrange(1,11)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> you hear some noises that scare you. you run away like a pansy loosing %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval

    if request.form["button"] == "loot":
        no_whammies = random.randrange(1,3)
        if no_whammies == 1:
            goldval = random.randrange(2,6)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='greentext'>Earned %s gold from looting a random person! you might want to reevaluate your life. (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] += goldval
        if no_whammies == 2:
            goldval = random.randrange(2,5)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> The person you tried to mug fights back! serves you right. you loose %s gold (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval

    if request.form["button"] == "casino":
        no_whammies = random.randrange(1,3)
        if no_whammies == 1:
            goldval = random.randrange(10,101)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='greentext'>Earned %s gold from the casino! lady luck has been kind to you! (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] += goldval
        
        if no_whammies == 2:
            goldval = random.randrange(10,101)
            now=datetime.datetime.now()
            timestamp=now.strftime("%B %d %Y %I:%M %p")
            event_log= "<p class='redtext'> you've lost %s gold from the casino! lady luck, why have you forsaken me! (%s)</p>" %(str(goldval),timestamp)
            session["act_log"].append(event_log)
            session["gold_count"] -= goldval
        



    return redirect("/")

@app.route("/restart")
def restart_game():
    session.clear()
    return redirect("/")




if __name__=="__main__":
    
    app.run(debug=True) 