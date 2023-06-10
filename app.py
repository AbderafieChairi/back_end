#flask app
from flask import Flask,request,jsonify
from tools import predict,getNext
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#cors allow all



@app.route('/')
def hello_world():
    response = jsonify({'next':"hello world"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response




@app.route('/next',methods=['POST'])
def next():
    json = request.get_json()
    symptoms = [i.replace(' ','_') for i in json['symptoms']]
    # symptoms=symptoms.split(',')
    response = jsonify({'next':getNext(symptoms)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/get',methods=['POST'])
def chat_bot():
    json = request.get_json()
    symptoms =json['symptoms']
    print(symptoms)
    return jsonify({'illness':predict(symptoms)})


if __name__ == '__main__':
    app.run(debug=True)