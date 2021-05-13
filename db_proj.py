import sqlite3
from sqlite3 import Error
import pandas as pd

def appendInfo(text, confidence, result):
    print(text,confidence,result)
    conn = sqlite3.connect('results.db')
    
    print("Opened database successfully")

    conn.execute(
            '''CREATE TABLE IF NOT EXISTS RESULTS
                (
                TEXT           TEXT    NOT NULL,
                CONFIDENCE     REAL     NOT NULL,
                RESULT        CHAR(50));'''
        )
    
    # conn.execute(
    #         '''CREATE TABLE IF NOT EXISTS RESULTS
    #             (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
    #             TEXT           TEXT    NOT NULL,
    #             CONFIDENCE     REAL     NOT NULL,
    #             RESULT        CHAR(50));'''
    #     )

    sql = '''INSERT INTO RESULTS(text, confidence, result) values(?,?,?)'''

    cur = conn.cursor()
    cur.execute(sql, (text, confidence, result))

    conn.commit()
    conn.close()

def readData():
    conn = sqlite3.connect('results.db')
    
    print("Opened database successfully")
    
    # cur = conn.cursor()
    # cur.execute("SELECT * FROM results")

    # rows = cur.fetchall()

    rows = pd.read_sql_query("SELECT * FROM results", conn)
    
    return rows