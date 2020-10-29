from flask import Flask,g

app = Flask(__name__)
app.debug = True


  
@app.route("/") #어디로 갈지 지정해주는 부분
def example():
  return render_template("example.html")


if __name__ == '__main__':
  aap.run()

