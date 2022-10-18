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
	sqlCreateTable = "create table " + name_Table + " (id text, carInsurance int, gym int, internet int, phone int, loans int);"

	# Create a table in PostgreSQL database
	cursor.execute(sqlCreateTable)
	conn.commit()

	# This prints out all the columns in the table
	sql= """ SELECT * FROM """ + name_Table + """ ; """
	cursor.execute(sql)
	column_names = [desc[0] for desc in cursor.description]

	#for i in column_names:
		#print(i)

	# Close the connection
	conn.commit()
	conn.close()

#########################################################################
def insertDataDB(tableName, name, carInsurance, gym, internet, phone, loans):
	# Define our connection string
	conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

	# Get a connection, if a connection cannot be made, an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	conn.autocommit = True
	cursor = conn.cursor()

	postgres_insert_query = """ INSERT INTO """ + tableName + """(id, carInsurance, gym, internet, phone, loans) 
	                            VALUES ( """ + """ \' """ + name + """ \', """ + """ \' """  + carInsurance + """ \', """ + """ \' """ + gym + """ \', """ + """ \' """ + internet + """ \', """ + """ \' """ + phone + """ \', """ + """ \' """ + loans + """ \' """ + """)"""
	cursor.execute(postgres_insert_query)

	# Print out the values in the table
	cursor.execute(""" SELECT * FROM """ + tableName + """;""")
	conn.commit()
	results = cursor.fetchall()
	for result in results:
		print("Id = ", result[0], )
		print("Car Insurance = ", result[1])
		print("Gym = ", result[2])
		print("Internet = ", result[3])
		print("Phone = ", result[4])
		print("Loans = ", result[5])

#########################################################################
def insertDataDBOtherPayments(tableName):
	# Define our connection string
	conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

	# Get a connection, if a connection cannot be made, an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	conn.autocommit = True
	cursor = conn.cursor()

	postgres_insert_query = """ INSERT INTO """ + tableName + """(id, carInsurance, gym, internet, phone, loans) 
	                            VALUES ( """ + """ \' """ + name + """ \', """ + """ \' """  + carInsurance + """ \', """ + """ \' """ + gym + """ \', """ + """ \' """ + internet + """ \', """ + """ \' """ + phone + """ \', """ + """ \' """ + loans + """ \' """ + """)"""
	cursor.execute(postgres_insert_query)

	# Print out the values in the table
	cursor.execute(""" SELECT * FROM """ + tableName + """;""")
	conn.commit()
	results = cursor.fetchall()
	for result in results:
		print("Id = ", result[0], )
		print("Car Insurance = ", result[1])
		print("Gym = ", result[2])
		print("Internet = ", result[3])
		print("Phone = ", result[4])
		print("Loans = ", result[5])

#########################################################################
# Print values in table
def printValuesInTable():
	# Define our connection string
	conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

	# Get a connection, if a connection cannot be made, an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	conn.autocommit = True
	cursor = conn.cursor()

	results = cursor.fetchall()
	for result in results:
		print("Id = ", result[0], )
		print("Car Insurance = ", result[1])
		print("Gym = ", result[2])
		print("Internet = ", result[3])
		print("Phone = ", result[4])
		print("Loans = ", result[5])

#########################################################################
#########################################################################

if __name__ == "__main__":
	# Future version: check for invalid characters as input
	val = input("Is this your first time running this program: [yes | no] ")
	if ("yes" in val):
		print("process")
	elif("no" in val):
		print("no")

	print("******************************************************************")
	print("Welcome to increaseCreditScore")
	print("Tool Description")
	print("******************************************************************")

	#val_tableName = input("Please enter your Table Name: ")
	# Run this statement once to initialize, need to find more permanent solution
	#connectDBCreateTable(val_tableName)

	#val_userName = input("What is your name: ")
	#print('Please enter the following information (per month), if you do not have something that was asked, enter 0')
	#print('For example, if you do not have car insurance, enter 0 when prompted', "\n")

	#val_carInsurance = input("What is the monthly amount that you pay for your car insurance: [Round up]  ")
	#val_gym = input("What is the monthly amount that you pay for your gym membership: [Round up]  ")
	#val_internet = input("What is the monthly amount that you pay for your internet: [Round up]  ")
	#val_phone = input("What is the monthly amount that you pay for your phone plan: [Round up]  ")
	#val_loans = input("What is the monthly amount that you pay for any loans (OSAP/PERSONAL): [Round up]  ")
	val_other = input ("Do you have any other monthly payments on your credit card: [yes | no] ")

	if ('yes' in val_other):
		val_other = input("Please enter the name of the payment: ")
		val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": ")
		val_other1 = input("Do you have anymore payments: [yes | no]  ")

		# Insert values from user into Database (for other payments)
		# insertDataDBOtherPayments(val_tableName)

		while ('yes' in val_other1):
			val_other = input("Please enter the name of the payment: ")
			val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": ")
			val_other1 = input("Do you have anymore payments: [yes | no]  ")

	elif('no' in val_other):
		# Insert values from user into Database
		insertDataDB(val_tableName, val_userName, val_carInsurance, val_gym, val_internet, val_phone, val_loans)
