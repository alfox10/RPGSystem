from flask import Flask
from threading import Thread
from flask import jsonify, request
import dbmanager

app = Flask('')
conn = None

class inventoryClass:
  description = None
  effect = None
  qt = None

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

@app.route('/api/v1/mork_attributes', methods=['POST'])
def get_attributes():
  request_data = request.get_json()
  p_id = request_data['id']
  p_data = (p_id,)
  pg_dict = {}
  res = dbmanager.retrieve_attributes(p_data)
  pg_dict["agility"] = res[0][0]
  pg_dict["presence"] = res[0][1]
  pg_dict["strength"] = res[0][2]
  pg_dict["toughness"] = res[0][3]
  return jsonify(pg_dict)


@app.route('/api/v1/stats', methods=['POST'])
def player_stats():
  request_data = request.get_json()
  p_id = request_data['id']
  p_data = (p_id,)
  res = dbmanager.retrieve_player_stat(p_data)
  pg_dict = {}
  pg_dict["hp"] = res[0][0]
  pg_dict["max_hp"] = res[0][1]
  pg_dict["omens"] = res[0][2]
  pg_dict["max_omens"] = res[0][3]
  pg_dict["name"] = res[0][4]
  pg_dict["pg_class"] = res[0][5]
  pg_dict["class_type"] = res[0][6]
  pg_dict["level"] = res[0][7]
  pg_dict["exp"] = res[0][8]
  return jsonify(pg_dict)

@app.route('/api/v1/inventory', methods=['POST'])
def player_inventory():
  request_data = request.get_json()
  p_id = request_data['id']
  p_data = (p_id,)
  iv_dict = []
  res = dbmanager.retrieve_player_inventory(p_data)
  idx = 0
  for item in res:
    idx +=1
    item_d = {}
    item_d["description"] = item[0]
    item_d["effect"] = item[1]
    item_d["qt"] = item[2]
    item_d["icon"] = item[3]
    item_d["is_equipped"] = item[4]
    iv_dict.append(item_d)
  res_dict ={"itemFormatList": iv_dict}
  return jsonify(res_dict)

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

	
if __name__ == '__main__':
    print("Starting Web Server")
    keep_alive()