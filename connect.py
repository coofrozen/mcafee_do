import mysql.connector
from mysql.connector import Error
from datetime import datetime

def connect(qu):
    """ Connect to MySQL database """
    today = datetime.today()
    dt_string = today.strftime("%d/%m/%Y %H:%M:%S")
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='isec_reporting',
                                       user='root',
                                       password='cofree@21')
        if conn.is_connected():
            print('Connected to MySQL database')
            cursor = conn.cursor()
            cursor.execute(qu)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')

            conn.commit()

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
