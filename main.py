from flask import Flask
from threading import Thread
from flask import jsonify, request
from dbmanager import create_connection

app = Flask('')
conn = None

@app.route('/')
def home():
    return '''<p><h1>RPG System API homepage</h1></p><p><h3>not really usefull</h3></p>'''

@app.route('/api/v1/player', methods=['GET'])
def get_players():
  results = ""
  global conn
  if conn is None:
    db_conn()
  cur = conn.cursor()
  cur.execute("SELECT * FROM player")
  results = cur.fetchall()
  return jsonify(results)

@app.route('/api/v1/credentials', methods=['POST'])
def check_credentials():
  res = {"response" : ""}
  global conn
  if conn is None:
    db_conn()
  cur = conn.cursor()
  request_data = request.get_json()
  print(request_data)
  username = request_data['username']
  password = request_data['password']
  data = (username, password)
  sql = """ SELECT id FROM player WHERE username=? AND password=? """
  query_res = cur.execute(sql, data).fetchall()
  if len(query_res) < 1:
    res["response"] = 0  
  else:
      for row in query_res:
        res["response"] = row[0]
  return jsonify(res)

def db_conn():
  global conn
  conn = create_connection('rpgsystem.db')

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
	
if __name__ == '__main__':
    print("Starting Web Server")
    keep_alive()