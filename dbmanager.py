import sqlite3
from sqlite3 import Error

conn = None
database = r"rpgsystem.db"

def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    global conn
    global database
    conn = None
    try:
        conn = sqlite3.connect(database, check_same_thread=False)
        return conn
    except Error as e:
        print(e)


def return_all_players():
    global conn
    if conn is None:
        create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM player")
    return cur.fetchall()

def check_user_credential(data):
    global conn
    if conn is None:
        create_connection()
    cur = conn.cursor()
    result = 0;
    sql = """ SELECT id FROM player WHERE username=? AND password=? """
    query_res = cur.execute(sql, data).fetchall()
    for row in query_res:
        result = row[0]
    return result

def retrieve_player_inventory(p_id):
    global conn
    if conn is None:
        create_connection()
    cur = conn.cursor()
    sql = """ select i.description, i.effect, vv.qt, i.icon, vv.is_equipped from items i inner join (select v.qt, v.is_equipped, v.item_id from inventory v where v.player_id=?) as vv on vv.item_id=i.id """
    return cur.execute(sql, p_id).fetchall()

def retrieve_player_stat(p_id):
    global conn
    if conn is None:
        create_connection()
    cur = conn.cursor()
    sql = """ SELECT hp, max_hp, omens, max_omens, name, class, class_type, level, exp FROM player_stats WHERE player_id=? """
    return cur.execute(sql, p_id).fetchall()

""" def insert_into_player_table(conn, data):
  sql = ''' INSERT INTO player(username,password) VALUES(?,?) '''
  cur = conn.cursor()
  cur.execute(sql, data)
  conn.commit()
  return cur.lastrowid """


def main():
    print("Welcome to dbManager, call functions to use this")


if __name__ == '__main__':
    main()
