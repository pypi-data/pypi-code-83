import pyodbc

class Connection(object):
    """Class to connect to any database server
    :parameter server name & database name (optional)"""
    
    
    """
    def __del__(self):
        
        if self.conn:
            self.conn.commit()
            self.conn.close()
    """
    # Method to connect to the server
    def connect(self, server_name, timeout=5):

        server_name = server_name.lower().replace('.win.ia55.net', '') + '.win.ia55.net'
        retry_count = 0
        SQL_CONN_RETRY_COUNT = 1 
        while retry_count < SQL_CONN_RETRY_COUNT:
            # try:
            connectionstring = 'DRIVER={Easysoft ODBC-SQL Server};Server='+server_name+';UID=;PWD=;ServerSPN=MSSQLSvc/'+server_name+';APP=dbcnames;'
            conn = pyodbc.connect(connectionstring, timeout=timeout)
            conn.autocommit = True
            self.conn = conn
            return conn
            # except Exception as ex:
            #     print("Error while creating database connection to {} server {}, trying again {}".format(server_name, str(ex), retry_count))
            retry_count += 1

        return None



# conn = Connection()
# cn = conn.connect('dbmonitor5b.win.ia55.net')
# cnxn = pyodbc.connect('DRIVER={Easysoft ODBC-SQL Server};Server=DBGELBASEDEVNYC;UID=;PWD=;APP=test;ServerSPN=MSSQLSvc/reins')
# cursor = cnxn.cursor()
# print(cursor.execute('select @@servername').fetchall())

connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};Server=dbmonitor5b.win.ia55.net;database=master;Trusted_Connection=yes;'
con = pyodbc.connect(connection_string)
cursor = cnxn.cursor()
print(cursor.execute('select @@servername').fetchall())

# cur = cn.cursor()
# cur.execute("select @@servername")  # Execute the query
# records = cur.fetchall()
# print(records)


