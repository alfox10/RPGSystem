from flask import Flask
from threading import Thread
from flask import jsonify, request
import dbmanager

app = Flask('')
conn = None

@app.route('/')
def home():
    return '''<p><h1>RPG System API homepage</h1></p><p><h3>Page not really usefull</h3></p>'''

@app.route('/api/v1/player', methods=['GET'])
def get_players():
  results = dbmanager.return_all_players()
  return jsonify(results)

@app.route('/api/v1/credentials', methods=['POST'])
def check_credentials():
  res = {"response" : ""}
  request_data = request.get_json()
  username = request_data['username']
  password = request_data['password']
  data = (username, password)
  res["response"] = dbmanager.check_user_credential(data)
  return jsonify(res)

@app.route('/api/v1/stats', methods=['POST'])
def player_stats():
  request_data = request.get_json()
  p_id = request_data['id']
  p_data = (p_id,)
  res = dbmanager.retrieve_player_stat(p_data)
  return jsonify(res)

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
	
if __name__ == '__main__':
    print("Starting Web Server")
    keep_alive()