from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
   
   return "OK"

if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0', port=8081)