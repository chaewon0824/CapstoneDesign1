from flask import Flask,render_template,request,Response
#from parlai.agents.local_human.local_human import *
#from parlai.scripts.interactive import *
#from flask_socketio import SocketIO,send,emit
import socket


HOST = '127.0.0.1'
PORT =  5000
BUF_SIZE = 1024

app = Flask(__name__)
app.debug = True
#app.config['SECRET_KEY'] = 'secret'
#socketio = SocketIO(app)



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


"""
@socketio.on('my event')
def handle_my_custom_event_recv(json,methods=['POST']):
  print('received my event: '+str(json))

def handle_my_custom_event_send(json,methods=['POST']):
  socketio.emit('my reponse',json,callback=messageRecevied)
"""


@app.route("/chatbot",methods=['POST'])
def req1():
  data = request.json
  sentence = data['sentence']
  print sentence
  return sentence

def answer_model(sentence):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  s.bind((HOST,PORT))
  s.listen()
  c, addr = s.accept()
  while True:
        if(sentence):
                c.sendall(sentence) #mirror_answer_to_model
		text = c.recv(BUF_SIZE) #answer_from_model
     		msg = text.decode()
                if(sentence=='EXIT'):
                        c.close()
			s.close()
                        break;
  return msg


@app.route("/example")
def example():
 # client = app.test_client()
 # response = client.get('/')
 # assert respnse.status_code == 200
 # text = ""
 # return render_template("example.html",textData=text)
  return render_template("example.html")

if __name__ == '__main__':
 # socketio.run(app,host='0.0.0.0')
  app.run(host='0.0.0.0')
