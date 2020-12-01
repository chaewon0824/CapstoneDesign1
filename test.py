from flask import Flask,render_template,request,Response
from socket import *


HOST = '127.0.0.1'
PORT =  5000
BUF_SIZE = 1024

app = Flask(__name__)
app.debug = True


serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind((HOST,PORT))
serverSock.listen()

connectionSock, addr = serverSock.accept()
print(str(addr),'Success Connection\n')


def send(sock,sendData):
	#sendData = input('>>>') #임시로 테스트를 위해 서버측에서 데이터를 콘솔로 입력하는 부분
	sock.send(sendData.encode()) #모델에게 data를 보냄
	
def receive(sock):
	recvData = sock.recv(BUF_SIZE) #모델한테 data 받음
	return recvData
	#print('Model: ',recvData.decode('utf-8')) #임시로 서버측 콘솔에 대답을 띄움
	
'''	
while True: #서버측 반복부분
	send(connectionSock)
	receive(connectionSock)
'''	



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
def req1(): #반복이 될지 안될지 모르겠다..이러면 소켓 연결은 되나?
  data = request.json
  send_sentence = data['sentence']
  send(connectionSock,send_sentence) #모델에게 매직미러에서 받은 데이터를 보냄
  sentence = receive(connectionSock) #여기서 함수의 리턴값 = 모델에게 받은 값, 그걸 sentence에 저장 
  print sentence
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
