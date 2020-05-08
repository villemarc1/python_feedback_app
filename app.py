from flask import Flask,jsonify,request,render_template

app = Flask(__name__)
app.debug = False


@app.route('/')
def home():
  return render_template('index.html')

app.run()
