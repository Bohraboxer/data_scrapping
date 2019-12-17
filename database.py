import sqlite3

# connection to myquotes.db
#if does not exist, it will create one
conn=sqlite3.connect('myquotes.db') 

# cursor helps us take advantage of all the functions
curr=conn.cursor()

# creating a table and adding columns
curr.execute("""Create table quotes_tb(
	title.text,
	author text,
	tag text
	)""")

#to make sure that
#the above are run when .py file is connected
conn.commit()

#closing the connection
conn.close()