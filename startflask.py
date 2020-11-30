from flask import Flask,render_template,request,Response
from socket import *


HOST = '127.0.0.1'
PORT =  5000
BUF_SIZE = 1024

app = Flask(__name__)
app.debug = True

def send(sock):
	sendData = input('>>>') #임시로 테스트를 위해 서버측에서 데이터를 콘솔로 입력하는 부분
	sock.send(sendData.encode())
	
def receive(sock):
	recvData = sock.recv(BUF_SIZE)
	print('Model: ',recvData.decode('utf-8')) #임시로 서버측 콘솔에 대답을 띄움

serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind((HOST,PORT))
serverSock.listen()

connectionSock, addr = serverSock.accept()
print(str(addr),'Success Connection\n')

while True: #서버측 반복부분
	send(connectionSock)
	receive(connectionSock)
	


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
#  print sentence
  return sentence



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
