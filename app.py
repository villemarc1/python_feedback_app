from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]


@app.route('/')
def home():
  return render_template('index.html')

app.run(port=5000)
