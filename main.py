# Author: Soundarya Srinivasagan
# Date: October 16th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help the user strategize their income to effectively increase credit score

import psycopg2
import sys

def connectDBCreateTable(name_Table):
	# Define our connection string
	conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

	# Get a connection, if a connection cannot be made, an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	conn.autocommit = True
	cursor = conn.cursor()

	# Create table statement
	sqlCreateTable = "create table " + name_Table + " (id bigint, title varchar(128), summary varchar(256), story text);"

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

if __name__ == "__main__":
	# Future version: check for invalid characters as input
	val = input("Is this your first time running this program: [yes | no] ")
	if ("yes" in val):
		val_tableName = input("Please enter your Table Name: ")
		# Run this statement once to initialize, need to find more permanent solution
		connectDBCreateTable(val_tableName)

	elif("no" in val):
		print("no")


