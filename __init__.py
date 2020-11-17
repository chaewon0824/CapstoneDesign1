from flask import Flask,render_template,request,Response
from flask_restful import Resource,Api

app = Flask(__name__)
app.debug = True
api = Api(app)


@app.route("/chatbot",methods=['POST'])
def req1():
  if request.method == 'POST':
      textData = request.form['sentence']	
  return "POST delivery {}".format(textData)

@app.route("/")
def example():
 # client = app.test_client()
 # response = client.get('/')
 # assert respnse.status_code == 200
 # text = ""
 # return render_template("example.html",textData=text)
  return render_template("example.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0')
