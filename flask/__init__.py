from flask import Flask,g

app = Flask(__name__)
app.debug = True

@app.before_request
def before_request():
  g.str="한글" 
  
@app.route("/") #어디로 갈지 지정해주는 부분



