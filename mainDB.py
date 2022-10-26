# Author: Soundarya Srinivasagan
# Date: October 17th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help create the main database that will store all the 'family's' information

# We need this python package to be able to communicate with the PostgreSQL Database
import psycopg2

########################################################################################################################
# Description: This function returns a cursor which can be used to initiate a connection to the database and perform SQL operations
# Input:
# Output: Returns cursor which is used throughout script to connect to DB and execute SQL statements
########################################################################################################################
def connectToDB():
	# Define our connection string
	conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

	# Get a connection, if a connection can't be made, an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	conn.autocommit = True
	cursor = conn.cursor()

	return cursor

########################################################################################################################
# Description: This function implements the CREATE TABLE SQL command
# Input: name_Table [String] = Name of the table entered by the user
# 		 dictOfValues [Dict of Strings: Ints] = Dict of values containing user input
# Output: Creates main table which stores all bills and their payment amount
########################################################################################################################
def connectDBCreateTable(name_Table, dictOfValues):
	local_cursor = connectToDB()

	# Create table statement
	sqlCreateTable1 = """ CREATE TABLE """ + name_Table
	sqlCreateTable2 = """ (id text, carInsurance int, gym int, internet int, phone int, loans int, """

	key = list(dictOfValues.keys())
	lastElement = key[-1]

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
	local_cursor.execute(sqlCreateTable)

########################################################################################################################
# Description: This function implements the INSERT INTO SQL command
# Input: tableName [String] = Name of the table entered by the user
# 		 name [String] = Name of user
# 		 carInsurance, gym, internet, phone, loans [INT] = Values entered by user for each payment
# Output: Inserts these values into DB table
########################################################################################################################
def insertDataDB(tableName, name, carInsurance, gym, internet, phone, loans):
	local_cursor = connectToDB()
	postgres_insert_query = """ INSERT INTO """ + tableName + """(id, carInsurance, gym, internet, phone, loans) 
	                            VALUES ( """ + """ \' """ + name + """ \', """ + """ \' """  + carInsurance + """ \', """ + """ \' """ + gym + """ \', """ + """ \' """ + internet + """ \', """ + """ \' """ + phone + """ \', """ + """ \' """ + loans + """ \' """ + """)"""

	local_cursor.execute(postgres_insert_query)

########################################################################################################################
# Description: This function implements the UPDATE SQL command
# Input:tableName [String] = Name of the table entered by the user
# 	    user [String] = Name of user
# 		dictOfValues [Dict of Strings: Ints] = Dict of values containing user input
# Output: Updates other payments in the main DB as entered by the user
########################################################################################################################
def insertDataDBOtherPayments(tableName, user, dictOfValues):
	local_cursor = connectToDB()

	key = list(dictOfValues.keys())
	lastElement = key[-1]

	# Use Update statement so that the same row could be updated
	postgres_insert_query_1T = """ UPDATE """ + tableName + """ SET """
	postgres_insert_query_2T = """  """
	postgres_insert_query_3T = """  WHERE id = """ + """ ' """ + user + """ ' """
	postgres_insert_query_4T = """ ; """
	for keys, values in dictOfValues.items():
		part1 = """ = """
		if (keys == lastElement):
			part4 = """  """
			postgres_insert_query_2T = postgres_insert_query_2T + keys + part1 + values + part4
		else:
			part4 = """ , """
			postgres_insert_query_2T = postgres_insert_query_2T + keys + part1 + values + part4

	postgres_insert_query = postgres_insert_query_1T + postgres_insert_query_2T + postgres_insert_query_3T + postgres_insert_query_4T
	local_cursor.execute(postgres_insert_query)

########################################################################################################################
# Description: This function returns all the column headers in the database table as a list of tuple
# Input: val_tableName [String] = Name of the table entered by the user
# 		 val_userName [String] = Name of user
# Output: Results returns all the column headers of the database table as a list of tuples
########################################################################################################################
# Print values in table
def printValuesInTable(val_tableName, val_userName):
	local_cursor = connectToDB()
	sql = """SELECT COLUMN_NAME FROM """ + """ INFORMATION_SCHEMA.COLUMNS """ + """ WHERE TABLE_NAME = """ + """ \'""" + val_tableName + """\' """ + """ ORDER BY ORDINAL_POSITION """ + """ ; """
	local_cursor.execute(sql)
	results = local_cursor.fetchall()

	return results

########################################################################################################################
# Description: This function implements the ALTER TABLE SQL command
# Input: tableName [String] = Name of the table entered by the user
#  		 user [String] = Name of user
#        otherItemsList [Dict of Strings: Ints] = Stores the other payments
# Output: Alters the main DB table with other payments that the user may have
########################################################################################################################
def alterTableToAddMoreColumns(tableName, user, otherItemsList):
	local_cursor = connectToDB()

	val_other = input("Please enter the name of the payment:  ")
	val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": [Round up]  ")
	print("\n")
	otherItemsList.update({val_other : val_other_amount})
	val_other1 = input("Do you have anymore payments: [y | n]  ")

	while ('y' in val_other1):
		val_other = input("Please enter the name of the payment: ")
		val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": [Round up]  ")
		print("\n")
		otherItemsList.update({val_other : val_other_amount})
		val_other1 = input("Do you have anymore payments: [y | n]  ")

	key = list(otherItemsList.keys())
	lastElement = key[-1]

	# Use Update statement so that the same row could be updated
	postgres_insert_query_1T = """ ALTER TABLE """ + tableName
	postgres_insert_query_2T = """  """
	postgres_insert_query_3T = """ ADD """
	postgres_insert_query_4T = """ ; """

	for keys in otherItemsList:
		type = """ int """
		#space = """  """
		if (keys == lastElement):
			part4 = """  """
			postgres_insert_query_2T = postgres_insert_query_2T + keys + type + part4
		else:
			part4 = """ , """
			postgres_insert_query_2T = postgres_insert_query_2T + keys + type + part4 + postgres_insert_query_3T

	postgres_insert_query = postgres_insert_query_1T + postgres_insert_query_3T + postgres_insert_query_2T + postgres_insert_query_4T
	local_cursor.execute(postgres_insert_query)

	# Update values for all the keys in the dict
	insertDataDBOtherPayments(tableName, user, otherItemsList)

########################################################################################################################
# Description: This function collects information on bill payments from the user and uses the other functions in this document to create/update the main table
# Input: val_tableName [String] = Name of the table entered by the user
#   	 val_userName [String] = Name of user
#        flag [Boolean] = If True it will create a new table, if false, it will alter the current table in the db
# Output:
########################################################################################################################
def query_billsCollect(val_tableName, val_userName, flag):
	# Dictionary to add all other types of payments
	otherItemsList = {}

	print("\n")
	print('Please enter the following information (per month), if you do not have something that was asked, enter 0')
	print('For example, if you do nt have car insurance, enter 0 when prompted', "\n")

	val_carInsurance = input("What is the monthly amount that you pay for your car insurance: [Round up]  ")
	val_gym = input("What is the monthly amount that you pay for your gym membership: [Round up]  ")
	val_internet = input("What is the monthly amount that you pay for your internet: [Round up]  ")
	val_phone = input("What is the monthly amount that you pay for your phone plan: [Round up]  ")
	val_loans = input("What is the monthly amount that you pay for any educational loans (OSAP): [Round up]  ")
	print("\n")

	val_other = input ("Do you have any other monthly payments on your credit card: [y | n] ")

	if (('y' in val_other) and (flag == False)):
		# Insert values from user into Database
		insertDataDB(val_tableName, val_userName, val_carInsurance, val_gym, val_internet, val_phone, val_loans)
		alterTableToAddMoreColumns(val_tableName, val_userName, otherItemsList)
		print("\n")

	elif ('y' in val_other):
		val_other = input("Please enter the name of the payment:  ")
		val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": [Round up]  ")
		print("\n")
		otherItemsList.update({val_other : val_other_amount})
		val_other1 = input("Do you have anymore payments: [y | n]  ")

		while ('y' in val_other1):
			val_other = input("Please enter the name of the payment: ")
			val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": [Round up]  ")
			print("\n")
			otherItemsList.update({val_other : val_other_amount})
			val_other1 = input("Do you have anymore payments: [y | n]  ")

		# See if a new table is necessary
		if (flag == True):
			# Run this statement once to initialize, need to find more permanent solution
			connectDBCreateTable(val_tableName, otherItemsList)

			# Insert values from user into Database
			insertDataDB(val_tableName, val_userName, val_carInsurance, val_gym, val_internet, val_phone, val_loans)

			# Insert values from user into Database (for other payments)
			insertDataDBOtherPayments(val_tableName, val_userName, otherItemsList)

			print("\n")

		elif (flag == False):
			# Insert values from user into Database
			insertDataDB(val_tableName, val_userName, val_carInsurance, val_gym, val_internet, val_phone, val_loans)

			# Insert values from user into Database (for other payments)
			insertDataDBOtherPayments(val_tableName, val_userName, otherItemsList)

			print("\n")

	elif ('n' in val_other):
		# See if a new table is necessary
		if (flag == True):
			# Run this statement once to initialize, need to find more permanent solution
			connectDBCreateTable(val_tableName, otherItemsList)

			# Insert values from user into Database
			insertDataDB(val_tableName, val_userName, val_carInsurance, val_gym, val_internet, val_phone, val_loans)

			# Insert values from user into Database (for other payments)
			insertDataDBOtherPayments(val_tableName, val_userName, otherItemsList)

			print("\n")

		elif (flag == False):
			# Insert values from user into Database
			insertDataDB(val_tableName, val_userName, val_carInsurance, val_gym, val_internet, val_phone, val_loans)

			print("\n")
