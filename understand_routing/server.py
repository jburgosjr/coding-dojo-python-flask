from flask import Flask
app = Flask (__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "dojo"

@app.route('/say/<word>')
def say(word):
    return "hi "+ word

@app.route('/repeat/<times_repeat>/<repeat_str>')
def repstr(times_repeat,repeat_str):
    post_repeat = ""
    for i in range(int(times_repeat)):
        post_repeat += repeat_str+" "
    return post_repeat

if __name__=="__main__":
    
app.run(debug = True)

