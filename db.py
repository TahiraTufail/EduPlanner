import pypyodbc as odbc

DRIVER_NAME= 'ODBC Driver 18 for SQL Server'
SERVER_NAME= 'Tahira-Tufail\\SQLEXPRESS01'
DATABASE_NAME = 'EduPlanner'

connection_string = (
    f"DRIVER={{{DRIVER_NAME}}};"
    f"SERVER={SERVER_NAME};"
    f"DATABASE={DATABASE_NAME};"
    "Trusted_Connection=yes;"  
    "TrustServerCertificate=yes;"  
)
conn = odbc.connect(connection_string)
# cursor = conn.cursor()
# cursor.execute(f"insert into student (rollNumber, programregistered, firstName, lastName, semester, age) values(001 , 'CS', 'Tahira', 'Tufail', 4, 20)")
# conn.commit()
# cursor.execute("SELECT * FROM student ")
# results = cursor.fetchall()
# print(results)
cursor = conn.cursor()
print(cursor)
def get_cursor():
    return cursor
def close_connection():
    cursor.close()
    conn.close()