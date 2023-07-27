# # loading in modules
# import sqlite3
#
# # creating file path
# dbfile = 'sqlite.db'
# # Create a SQL connection to our SQLite database
# con = sqlite3.connect(dbfile)
#
# # creating cursor
# cur = con.cursor()
#
# # reading all table names
# table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
# # here is you table list
# print(table_list)
#
# for row in cur.execute("SELECT * FROM SECRET_CODE"):
#     print(row)
#
# # Be sure to close the connection
# con.close()

##################################################

import pandas as pd
import sqlite3
import sqlalchemy

try:
    conn = sqlite3.connect("sqlite.db")
except Exception as e:
    print(e)

#Now in order to read in pandas dataframe we need to know table name
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(f"Table Name : {cursor.fetchall()}")

df = pd.read_sql_query('SELECT * FROM SUCCESS_MESSAGE', conn)
print(df)
conn.close()

##############################

# import hashlib
#
# a_string = 'Hello I must tell you that I really like sucking on pickles'
#
# hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
# print(hashed_string)
# ##5d08f65a6e3df5e6461741704beaa9796f004d201430ba