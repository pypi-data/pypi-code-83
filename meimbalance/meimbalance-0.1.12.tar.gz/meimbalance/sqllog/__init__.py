from dotenv import load_dotenv
import pyodbc # Python interface for ODBC API         https://github.com/mkleehammer/pyodbc
import os
from datetime import datetime
import logging

def __get_connection():
    try:
        load_dotenv(verbose=False, override=True)
    except:
        logging.info('Error in load_dotenv')

    server=os.environ['IMBALANCE_LOG_SERVER']
    database=os.environ['IMBALANCE_LOG_DATABASE']
    username=os.environ['IMBALANCE_LOG_USERNAME']
    password=os.environ['IMBALANCE_LOG_PASSWORD']
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return connection

def log_files(filetype, filename, url, status, message):
    now = datetime.now()
    connection = __get_connection()
    cursor = connection.cursor()
    cursor.execute('insert into files(dt, filetype, filename, url, status, message) values(?, ?, ?, ?, ?, ?)', now, filetype, filename, url, status, message)
    connection.commit()

def log_files_forecast(filetype, filename, url, status, message,starttime,filecount=0,elapsedtime=0,year='0000',month='00',day='00',forecast='0000',windpark=''):
    message = message[0:4000]
    now = datetime.now()
    connection = __get_connection()
    cursor = connection.cursor()
    cursor.execute('insert into files(dt, filetype, filename, url, status, message, forecast,filecount,elapsedtime,year,month,day,starttime,windpark) values(?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?)', now, filetype, filename, url, status, message, forecast,filecount,elapsedtime,year,month,day,starttime,windpark)
    connection.commit()

def log(severity, message):
    now = datetime.now()
    connection = __get_connection()
    cursor = connection.cursor()
    cursor.execute('insert into logs(dt, severity, message) values(?, ?, ?)', now, severity, message)
    connection.commit()

# 
# Query the log database for a single row single column
#
def __get_sql_value(sql):
    connection = __get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor.fetchall():
        value = row.value
        break

    cursor.close()
    return value 
