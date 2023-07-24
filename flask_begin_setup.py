from flask import Flask,render_template,request
import mysql.connector
import newCodeSql
import json
from markupsafe import escape
import yfinance as yf

print("HELLO ")
app = Flask(__name__)
print(" HELLO ")
@app.route("/")
def hello_world():
    connection = newCodeSql.connection_db()
    cursor = newCodeSql.get_cursor(connection)
    return "<p> Connection with database established.  :) </p>"

""" @app.route("/create_table/<name>")
def table_creation(name):
    connection = newCodeSql.connection_db()
    cursor = newCodeSql.get_cursor(connection)
    new_table = newCodeSql.create_table(cursor,name)
    return 'New table %s' % name % ' created' """


@app.route("/volume_add-row", methods = ['GET','POST'])
def add_row(table_name):
    connection = newCodeSql.connection_db()
    cursor = newCodeSql.get_cursor(connection)
    import add_row_html_input
    if request.method == 'POST':
        json_str = add_row_html_input.get_data()
    mySql_insert_blank_row = """INSERT INTO movies (title,genre,release_year) 
                           VALUES 
                           """.join(json_str)
    cursor.execute(mySql_insert_blank_row)
    sql_select_Query = "select * from movies"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    rstring = []
    for rec in records:
        rstring.append("<h1>" + rec[0] + "</h1><br>")
    return "".join(rstring)
    

@app.route("/list-students")
def list_students():
    connection = mysql.connector.connect(host = 'localhost',
                                    database='Volume_2',
                                    user='Oakridge',
                                    password='password')
    cursor = connection.cursor()
    sql_select_Query = "select * from movies"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    #pprint.pprint(records[0][0])
    rstring = []
    for rec in records:
        rstring.append("<h1>" + rec[0] + "</h1><br>")
    return "".join(rstring)
    
@app.route("/get_stock_price/<name>")
def get_stock_price(name):
    data = yf.Ticker(name).info
    previousClosePrice = data['regularMarketPreviousClose']
    return str(previousClosePrice)
    

if __name__ == "__main__":
    app.degbug = True
    print(" Running main ")
    app.run()