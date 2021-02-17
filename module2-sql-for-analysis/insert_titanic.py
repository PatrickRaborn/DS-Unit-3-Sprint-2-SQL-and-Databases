'''A pipeline that transfers titanic.csv to sqlite3 to postgreSQL'''


import sqlite3
import psycopg2
import queries as q
import pandas as pd


df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'", ' ')


# Convert CSV to sqlite3 db
conn = sqlite3.connect('titanic.sqlite3')
curs = conn.cursor()
df.to_sql('titanic', con=conn)

sqlite_titanic_db = 'titanic.sqlite3'

DBNAME = "ubuzkhdk"
USER = "ubuzkhdk"
PASSWORD = "vh5-vhI9nfsiYdE-CUe64DaGhj6O6r9a"
HOST = "ziggy.db.elephantsql.com"

# sqlite database handler

titanic_db = 'titanic_db.sqlite3'

def lite_connect(sqlite_db):
    '''Returns sqlite connection'''
    sqlite_conn = sqlite3.connect(sqlite_db)
    return sqlite_conn

# PostGreSQL database handlers 

def pg_connect(dbname, user, password, host):
    '''Returns pg connection object'''
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                                password=password, host=host)
    return pg_conn

def create_cursor(conn):
    '''Returns cursor'''
    curs = conn.cursor()
    return curs

def execute_query(curs, query, reading=True):
    '''Executes query'''
    curs.execute(query)
    if reading:
        results = curs.fetchall()
        return results
    return 'This statement worked'

def add_passangers(pg_curs, passangers):
    '''Grabbing passangers from sqlite'''
    insert_passanger_statement ='''
    INSERT INTO titanic_table (
        Index_ID,
        Survived,
        PClass,
        Name,
        Sex,
        Age,
        SiblingsSpouses,
        ParentsChildren,
        Fare
    ) VALUES {};
    '''
    for i in passanger_list:
        pg_curs.execute(insert_passanger_statement.format(i))

if __name__ == "__main__":
    # create connection and cursor for pg
    pg_conn = pg_connect(DBNAME, USER, PASSWORD, HOST)
    pg_curs = create_cursor(pg_conn)
    # create connection and cursor for sl
    sl_conn = lite_connect(sqlite_titanic_db)
    sl_curs = create_cursor(sl_conn)
    # create PGS DB
    execute_query(pg_curs, q.create_titanic_table, reading=False)
    # select all rows from SQLite db
    passanger_list = execute_query(sl_curs, q.SELECT_ALL.format('titanic'))
    # insert all rows from SQLite to PostGreSQL
    add_passangers(pg_curs, passanger_list)
    # commit changes 
    pg_conn.commit()
    sl_conn.commit()