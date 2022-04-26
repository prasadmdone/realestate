import mysql.connector
# def DataUpdate(budget,area,name,email,phone,timeline,location):
def DataUpdate(budget):
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="info"
   )
  mycursor = mydb.cursor()
  # sql='CREATE TABLE info (budget VARCHAR,area VARCHAR,name VARCHAR,email VARCHAR,phone VARCHAR,timeline VARCHAR,location VARCHAR);'
  # sql='INSERT INTO info (budget,area,name,email,phone,timeline,location) VALUES ("{0}","{1}", "{2}","{3}","{4}","{5}","{6}","{7}","{8}");'.format(budget,area,name,email,phone,timeline,location)
  # sql='CREATE TABLE info (budget VARCHAR);'
  sql='INSERT INTO real_info (budget) VALUES {0})'.format(budget)
  mycursor.execute(sql)
  mydb.commit()

# import sqlite3
# from sqlite3 import Error


# def create_connection(db_file):
#    """ create a database connection to a SQLite database """
#    conn = None
#    try:
#        conn = sqlite3.connect(db_file)
#        print(sqlite3.version)
#    except Error as e:
#        print(e)
#    finally:
#        if conn:
#            conn.close()


# if __name__ == '__main__':
#    create_connection(r"C:\Users\Biju\Desktop\rasa\Banking service\sqlite3db.db")
   
# sqlite3.connect('sqlite3db')