from flask import Flask,render_template,request,Response
from flask_restful import Resource,Api

app = Flask(__name__)
app.debug = True
#api = Api(app)


@app.route("/chatbot",methods=['POST'])
def chatbot():
 # client = app.test_client()
 # response = client.get('/')
 # assert respnse.status_code == 200
 # text = ""
 # return render_template("example.html",textData=text)
  request.endpoint
  request.forms.
  return render_template("example.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0')
