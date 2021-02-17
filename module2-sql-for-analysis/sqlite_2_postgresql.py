"""A pipeline that transfers data from sqlite to postgreSQL"""

import sqlite3
import psycopg2
import queries as q


DBNAME = "lyypgvvq"
USER = "lyypgvvq"
PASSWORD = "xilq0uAz61dusT4E7Lom8IDfI91W-54N"
HOST = "ziggy.db.elephantsql.com"

# sqlite database handlers 

sqlite_rpg_db = 'rpg_db.sqlite3'

def lite_connect(sqlite_db):
    '''Returns sqlite connection'''
    sqlite_conn = sqlite3.connect(sqlite_db)
    return sqlite_conn



# PostGreSQL database handlers

def pg_connect(dbname, user, password, host):
    """Returns pg connection object"""
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                               password=password, host=host)
    return pg_conn

def create_cursor(conn):
    """Returns cursor"""
    curs = conn.cursor()
    return curs

def execute_query(curs, query, reading=True):
    """Executes query"""
    curs.execute(query)
    if reading:
        results = curs.fetchall()
        return results
    return "This statement worked!"

def add_characters(pg_curs, character_list):
    """Grabbing characters from sqlite"""
    insert_character_statement = """
      INSERT INTO charactercreator_character
      (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
      VALUES {};
    """
    for character in character_list:
        pg_curs.execute(insert_character_statement.format(character))


if __name__ == "__main__":
    # creates conn and curs for pg
    pg_conn = pg_connect(DBNAME, USER, PASSWORD, HOST)
    pg_curs = create_cursor(pg_conn)
    # creates conn and curs for sl
    sl_conn = lite_connect(sqlite_rpg_db)
    sl_curs = create_cursor(sl_conn)

    results = execute_query(pg_curs, q.create_character_table, reading=False)
    character_list = execute_query(sl_curs, q.SELECT_ALL.format('charactercreator_character'))
    add_characters(pg_curs, character_list)

    pg_conn.commit()
    sl_conn.commit()
