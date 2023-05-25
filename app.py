#flask app
from flask import Flask,request
from tools import predict,getNext
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def hello_world():
    return 'Hello World!'




@app.route('/next',methods=['POST'])
def next():
    json = request.get_json()
    symptoms =json['symptoms']
    return getNext(symptoms)

@app.route('/chat_bot',methods=['POST'])
def chat_bot():
    json = request.get_json()
    symptoms =json['symptoms']
    print(symptoms)
    # # using NLP extract intensity
    if symptoms[-1]["value"]>0.5:
        return predict(symptoms)
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)