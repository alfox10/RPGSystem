import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
def insert_into_player_table(conn, data):
  sql = ''' INSERT INTO player(username,password) VALUES(?,?) '''
  cur = conn.cursor()
  cur.execute(sql, data)
  conn.commit()
  return cur.lastrowid

def print_player_table(conn):
  cur = conn.cursor()
  cur.execute("SELECT * FROM player")
  results = cur.fetchall()
  print("results:")
  print("_ _ _ _ _ _")
  for results in results:
    print(results)
  print("_ _ _ _ _ _")

def main():
    database = r"rpgsystem.db"

    sql_create_player_table = """ CREATE TABLE IF NOT EXISTS player (
                                        id integer  PRIMARY KEY AUTOINCREMENT,
                                        username text NOT NULL,
                                        password text NOT NULL
                                    ); """


    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_player_table)
        p_1 = ('Rick', 'rpg1')
        insert_into_player_table(conn, p_1)
        p_1 = ('Nuz', 'rpg1')
        insert_into_player_table(conn, p_1)
        p_1 = ('Sara', 'rpg1')
        insert_into_player_table(conn, p_1)
        p_1 = ('Andrea', 'rpg1')
        insert_into_player_table(conn, p_1)
        print_player_table(conn)
        

    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    print("Init DB")
    main()
