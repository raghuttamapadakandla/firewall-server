import server
from server import app
import validation
from validation import callGPT
import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
 return 'pong', 200

@app.route('/test', methods=['POST'])
def home():
  print('---')
  print('ip')
  print(request.headers['X-Forwarded-For'])
  print('---')
  print('---')
  print('headers')
  print(request.headers)
  print('---')
  print('---')
  print('body')
  print(request.json)
  print('---')
  score = callGPT(request)
  if(score > 6):
    return 'forbidden', 403
  return 'ok', 200

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
