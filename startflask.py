from flask import Flask,render_template,request,Response
#from flask_restful import Resource,Api

app = Flask(__name__)
app.debug = True
#api = Api(app)

@app.route("/test",methods=['POST'])
def test():
  record = json.loads(request.data)
  new_records =[]
  with open('/tmp/data.txt','r') as f:
     data = f.read()
     records = json.loads(data)
  for r in records:
     if r['name'] == record['name']:
         r['email'] = record['email']
     new_records.append(r)
  with open('/tmp/data.txt','w') as f:
     f.write(json.dumps(new_records,indent=2))
  return jsonify(record)



@app.route("/chatbot",methods=['GET','POST'])
def req1():
  if request.method == 'GET':
      textData = request.args.get('sentence')
  if request.method == 'POST':
      record = json.loads(request.data)
      textData = record['sentence']
  return " hello, {}".format(textData)



@app.route("/example")
def example():
 # client = app.test_client()
 # response = client.get('/')
 # assert respnse.status_code == 200
 # text = ""
 # return render_template("example.html",textData=text)
  return render_template("example.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0')
