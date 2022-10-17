# Author: Soundarya Srinivasagan
# Date: October 16th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help the user strategize their income to effectively increase credit score

import psycopg2

########################################################################
def connectDBCreateTable(name_Table):
	# Define our connection string
	conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

	# Get a connection, if a connection cannot be made, an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	conn.autocommit = True
	cursor = conn.cursor()

	# Create table statement
	sqlCreateTable = "create table " + name_Table + " (id text, carInsurance int);"

	# Create a table in PostgreSQL database
	cursor.execute(sqlCreateTable)
	conn.commit()

	# This prints out all the columns in the table
	sql= """ SELECT * FROM """ + name_Table + """ ; """
	cursor.execute(sql)
	column_names = [desc[0] for desc in cursor.description]

	for i in column_names:
		print(i)

	# Close the connection
	conn.commit()
	conn.close()

########################################################################
def insertDataDB(tableName, name, carInsurance):
	# Define our connection string
	conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

	# Get a connection, if a connection cannot be made, an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	conn.autocommit = True
	cursor = conn.cursor()

	postgres_insert_query = """ INSERT INTO """ + tableName + """(id, carInsurance) VALUES ( """ + """ \' """ + name + """ \', """ + """ \' """  + carInsurance + """ \' """ + """)"""
	#record_to_insert = (name)
	cursor.execute(postgres_insert_query)

	# Print out the values in the table
	cursor.execute(""" SELECT * FROM """ + tableName + """;""")
	conn.commit()
	results = cursor.fetchall()
	for result in results:
		print("Id = ", result[0], )
		print("Car Insurance = ", result[1])


if __name__ == "__main__":
	# Future version: check for invalid characters as input
	val = input("Is this your first time running this program: [yes | no] ")
	if ("yes" in val):
		print("yes")
	elif("no" in val):
		print("no")

	print("******************************************************************")
	print("Welcome to increaseCreditScore")
	print("Tool Description")
	print("******************************************************************")

	val_tableName = input("Please enter your Table Name: ")
	val_userName = input("What is your name: ")
	print('Please enter the following information, if you do not have something that was asked, enter 0')
	print('For example, if you do not have car insurance, enter 0 when prompted', "\n")
	val_carInsurance = input("What is the amount for your Car Insurance: [Round up]  ")


	# Run this statement once to initialize, need to find more permanent solution
	connectDBCreateTable(val_tableName)

	insertDataDB(val_tableName, val_userName, val_carInsurance)
