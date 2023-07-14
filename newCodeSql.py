import sys
#sys.path.append("/usr/local/lib/python3.11/site-packages")
#sys.path.append("/usr/local/lib/python3.11/site-packages")
sys.path.append("/Users/srujanv/Desktop/vv/lib/python3.11/site-packages")
import mysql.connector
def connection_db():
    connection = mysql.connector.connect(host = 'localhost',
                                    database='Volume_2',
                                    user='Oakridge',
                                    password='password')
    if connection.is_connected():
        print('Stable connection',connection)
    else:
        print("FAILED to connect")
        sys.exit(1)
    cursor = get_cursor(connection)
    cursor.execute("select database();")
    record = cursor.fetchall()
    print(record)
    return connection 

def get_cursor(con):
    cursor = con.cursor()
    return cursor 

def create_table(cursor, tname):
    mySql_Create_Table_Query = """CREATE Table Chaitanya( 
                            Id int(9) NOT NULL,
                            Name varchar(250) NOT NULL,
                            Grade int(2) NOT NULL,
                            PRIMARY KEY (Id)) """
    cursor.execute(mySql_Create_Table_Query)
    print("Chaitanya Table created successfully ")
def insert_row(cursor,row):
    rowx = []
    for colv in row:
        rowx.append("'%s'" % colv if type(colv) == type("str") else str(colv) )
    print(rowx)
    row_string = ",".join(rowx)
    mySql_insert_query = """INSERT INTO Chaitanya (Id, Name, Grade) 
                           VALUES 
                            ( """ +  row_string + " ) "
    print(" INSERT QUERY ",mySql_insert_query)
    cursor.execute(mySql_insert_query)
    print(row[1], " row is inserted")

#Main Code
con = connection_db()
#create_table(cursor, None)

row = [
    [ 100,'Surya',121],
    [101,'Sateesh',990],
    [102,'sri',121]
]
for row1 in row:
    cursor = con.cursor()
    insert_row(cursor,row1)
con.commit()

sys.exit(1)
print("Inserted Surya's data")
mySql_insert_repeat_query = """INSERT INTO Chaitanya (Id, Name, Grade) 
                           VALUES 
                           (213019291, 'Sunara', 12)"""
cursor.execute(mySql_insert_repeat_query)
print("Inserted SUnara's data")

print(cursor.rowcount, "Record inserted successfully into Laptop table")

#Update function
    #First Select
mySql_select_Surya = """select * from Chaitanya where Id = 213019289"""
#cursor.execute(mySql_select_Surya)
print("Selected Surya")

mySql_update_Surya = '''UPDATE Chaitanya SET Name = 'Surya Sai' WHERE Id = 213019289 '''
#cursor.execute(mySql_update_Surya)
print("Updated Surya Sai")

#Delete Sunara
mySql_Delete_query = """Delete from Chaitanya where id = 213019291"""
#cursor.execute(mySql_Delete_query)
print("Sunara deleted")