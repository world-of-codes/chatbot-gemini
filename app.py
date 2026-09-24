from flask import Flask,render_template,request
from chat import talk
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route("/chat")
def call_gemini():
    pr=request.args.get("prompt")
    answer=talk(pr)
    return "<body bgcolor='yellow' text='green'><center><h1>{}</h1></center>\
           </body>".format(answer)        



if __name__=='__main__':
    app.run(debug=True)

