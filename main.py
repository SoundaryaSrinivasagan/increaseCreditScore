# Author: Soundarya Srinivasagan
# Date: October 16th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help the user strategize their income to effectively increase credit score

import psycopg2

########################################################################
def connectDBCreateTable(name_Table, userName, dictOfValues):
	# Define our connection string
	conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

	# Get a connection, if a connection cannot be made, an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	conn.autocommit = True
	cursor = conn.cursor()

	# Create table statement
	sqlCreateTable1 = """ create table """ + name_Table
	sqlCreateTable2 = """ (id text, carInsurance int, gym int, internet int, phone int, loans int, """

	key = list(dictOfValues.keys())
	lastElement = key[-1]
	# print(lastElement)

	part = """  """
	for keys in dictOfValues:
		part12 = keys
		part14 = """ int """
		part_space = """  """
		if (keys == lastElement):
			part13 = """  """
			part = part + part12 + part_space+ part14 + part13
		else:
			part13 = """ , """
			part = part + part12 + part_space + part14 + part13

	sqlCreateTable3 = part
	sqlCreateTable4 = """ ); """
	sqlCreateTable = sqlCreateTable1 + sqlCreateTable2 + sqlCreateTable3 + sqlCreateTable4

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
def insertDataDBOtherPayments(tableName, id, dictOfValues):
	conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

	# Get a connection, if a connection cannot be made, an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	conn.autocommit = True
	cursor = conn.cursor()

	# UPDATE bike SET full_day = 10 WHERE id = id;
	postgres_insert_query_1 = """ Update """ + tableName


	postgres_insert_query_1 = """ INSERT INTO """ + tableName

	# Configuring what columns to put the data in
	postgres_insert_query_20 = """ ( """
	postgres_insert_query_21 = """  """

	key = list(dictOfValues.keys())
	lastElement = key[-1]
	# print(lastElement)

	for keys in dictOfValues:
		part2 = keys
		if (keys == lastElement):
			part31 = """  """
			postgres_insert_query_21 = postgres_insert_query_21 + part2 + part31
		else:
			part32 = """ , """
			postgres_insert_query_21 = postgres_insert_query_21 + part2 + part32

	postgres_insert_query_22 = """ ) """
	postgres_insert_query_2 = postgres_insert_query_20 + postgres_insert_query_21 + postgres_insert_query_22

	#########-------------------------------------------------------------------------------------------------

	# Configuring the values for the respective columns
	postgres_insert_query_30 = """ VALUES ( """
	postgres_insert_query_31 = """  """

	for keys, values in dictOfValues.items():
		part41 = """ \' """
		part4 = values
		if (keys == lastElement):
			part42 = """ \' """
			postgres_insert_query_31 = postgres_insert_query_31 + part41 + part4 + part42
		else:
			part43 = """ \', """
			postgres_insert_query_31 = postgres_insert_query_31 + part41 + part4 + part43

	postgres_insert_query_32 = """ ) """
	postgres_insert_query_3 = postgres_insert_query_30 + postgres_insert_query_31 + postgres_insert_query_32

	cursor.execute(postgres_insert_query_1 + postgres_insert_query_2 + postgres_insert_query_3)

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

	val_tableName = input("Please enter your Table Name: ")
	val_userName = input("What is your name: ")
	print('Please enter the following information (per month), if you do not have something that was asked, enter 0')
	print('For example, if you do not have car insurance, enter 0 when prompted', "\n")

	val_carInsurance = input("What is the monthly amount that you pay for your car insurance: [Round up]  ")
	val_gym = input("What is the monthly amount that you pay for your gym membership: [Round up]  ")
	val_internet = input("What is the monthly amount that you pay for your internet: [Round up]  ")
	val_phone = input("What is the monthly amount that you pay for your phone plan: [Round up]  ")
	val_loans = input("What is the monthly amount that you pay for any loans (OSAP/PERSONAL): [Round up]  ")
	val_other = input ("Do you have any other monthly payments on your credit card: [yes | no] ")

	# Dictionary to add all other types of payments
	otherItemsList = {}

	if ('yes' in val_other):
		val_other = input("Please enter the name of the payment: ")
		val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": ")
		otherItemsList.update({val_other : val_other_amount})
		val_other1 = input("Do you have anymore payments: [yes | no]  ")

		while ('yes' in val_other1):
			val_other = input("Please enter the name of the payment: ")
			val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": ")
			otherItemsList.update({val_other : val_other_amount})
			val_other1 = input("Do you have anymore payments: [yes | no]  ")

		# Verify items in the dict
		# print(otherItemsList)

		# Run this statement once to initialize, need to find more permanent solution
		connectDBCreateTable(val_tableName, val_userName, otherItemsList)

		# Insert values from user into Database
		insertDataDB(val_tableName, val_userName, val_carInsurance, val_gym, val_internet, val_phone, val_loans)

		# Insert values from user into Database (for other payments)
		insertDataDBOtherPayments(val_tableName, val_userName, otherItemsList)

	elif('no' in val_other):
		# Run this statement once to initialize, need to find more permanent solution
		connectDBCreateTable(val_tableName, val_userName, otherItemsList)

		# Insert values from user into Database
		insertDataDB(val_tableName, val_userName, val_carInsurance, val_gym, val_internet, val_phone, val_loans)
