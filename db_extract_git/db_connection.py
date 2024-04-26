import pyodbc

def connect():
    # Connect to SQL Server
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=Server_name;'
                        'DATABASE=db_name;'
                        'UID=uid_name;'
                        'PWD=type_ur_pwd_here!')
    
    return conn