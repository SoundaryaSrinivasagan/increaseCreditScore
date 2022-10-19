# Author: Soundarya Srinivasagan
# Date: October 16th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help the user strategize their income to effectively increase credit score

import psycopg2

########################################################################
def connectToDB():
	# Define our connection string
	conn_string = "host='localhost' dbname='increasecreditscore' user='soundaryasrinivasagan' password='secret'"

	# Get a connection, if a connection cannot be made, an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	conn.autocommit = True
	cursor = conn.cursor()

	return cursor

########################################################################
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

#########################################################################
def insertDataDB(tableName, name, carInsurance, gym, internet, phone, loans):
	local_cursor = connectToDB()
	postgres_insert_query = """ INSERT INTO """ + tableName + """(id, carInsurance, gym, internet, phone, loans) 
	                            VALUES ( """ + """ \' """ + name + """ \', """ + """ \' """  + carInsurance + """ \', """ + """ \' """ + gym + """ \', """ + """ \' """ + internet + """ \', """ + """ \' """ + phone + """ \', """ + """ \' """ + loans + """ \' """ + """)"""

	local_cursor.execute(postgres_insert_query)

#########################################################################
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
	print(postgres_insert_query)
	local_cursor.execute(postgres_insert_query)

	# Fetching all the rows after the update
	sql = '''SELECT * from family'''
	local_cursor.execute(sql)
	print(local_cursor.fetchall())

#########################################################################
# Print values in table
def printValuesInTable():
	local_cursor = connectToDB()

	results = local_cursor.fetchall()
	for result in results:
		print("Id = ", result[0], )
		print("Car Insurance = ", result[1])
		print("Gym = ", result[2])
		print("Internet = ", result[3])
		print("Phone = ", result[4])
		print("Loans = ", result[5])

#########################################################################
def alterTableToAddMoreColumns(tableName, user):
	# Dictionary to add all other types of payments
	otherItemsList = {}
	local_cursor = connectToDB()

	val_other = input("Please enter the name of the payment:  ")
	val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": [Round up]  ")
	print("\n")
	otherItemsList.update({val_other : val_other_amount})
	val_other1 = input("Do you have anymore payments: [yes | no]  ")

	while ('yes' in val_other1):
		val_other = input("Please enter the name of the payment: ")
		val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": [Round up]  ")
		print("\n")
		otherItemsList.update({val_other : val_other_amount})
		val_other1 = input("Do you have anymore payments: [yes | no]  ")

	# ALTER TABLE Customers
	# ADD Email varchar(255);

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
	print(otherItemsList)
	insertDataDBOtherPayments(tableName, user, otherItemsList)


#########################################################################
def query_billsCollect_firstTime(val_tableName, val_userName, flag):
	# Dictionary to add all other types of payments
	otherItemsList = {}

	print("\n")
	print('Please enter the following information (per month), if you do not have something that was asked, enter 0')
	print('For example, if you do not have car insurance, enter 0 when prompted', "\n")

	val_carInsurance = input("What is the monthly amount that you pay for your car insurance: [Round up]  ")
	val_gym = input("What is the monthly amount that you pay for your gym membership: [Round up]  ")
	val_internet = input("What is the monthly amount that you pay for your internet: [Round up]  ")
	val_phone = input("What is the monthly amount that you pay for your phone plan: [Round up]  ")
	val_loans = input("What is the monthly amount that you pay for any educational loans (OSAP): [Round up]  ")
	print("\n")

	val_other = input ("Do you have any other monthly payments on your credit card: [yes | no] ")

	if (('yes' in val_other) and (flag == False)):
		# Insert values from user into Database
		insertDataDB(val_tableName, val_userName, val_carInsurance, val_gym, val_internet, val_phone, val_loans)

		alterTableToAddMoreColumns(val_tableName, val_userName)

		# Update values for all the keys in the dict
		# insertDataDBOtherPayments(val_tableName, val_userName, otherItemsList)

		print("\n")

	elif ('yes' in val_other):
		val_other = input("Please enter the name of the payment:  ")
		val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": [Round up]  ")
		print("\n")
		otherItemsList.update({val_other : val_other_amount})
		val_other1 = input("Do you have anymore payments: [yes | no]  ")

		while ('yes' in val_other1):
			val_other = input("Please enter the name of the payment: ")
			val_other_amount = input("What is the monthly amount that you pay for " + val_other + ": [Round up]  ")
			print("\n")
			otherItemsList.update({val_other : val_other_amount})
			val_other1 = input("Do you have anymore payments: [yes | no]  ")

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

	elif ('no' in val_other):
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


#########################################################################
if __name__ == "__main__":

	print("**********************************************************************************")
	print("Welcome to increaseCreditScore")
	print("Tool Description")
	print("**********************************************************************************")

	# Future version: check for invalid characters as input
	val = input("Is this your first time running this program: [yes | no] ")
	if ("yes" in val):
		val_tableName = input("Please enter your Group Name: ")
		val_userName = input("What is your name: ")
		query_billsCollect_firstTime(val_tableName, val_userName, True)

	elif("no" in val):
		val_tableName = input("Please enter your Group Name: ")
		val_decide = input("Do you want to update amount for bill payments [1] or Add user to your Family Table [2]: [ 1 | 2 ]  ")
		if ("1" in val_decide):
			val_userName = input("What is your name: ")
			val_update = input("What payment would you like to update: ")

		elif ("2" in val_decide):
			val_userName = input("What is your name: ")
			# This will not create a new group and add val_username to the same group
			query_billsCollect_firstTime(val_tableName, val_userName, False)
