# Author: Soundarya Srinivasagan
# Date: October 19th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help create the credit databases which consists of all the credit information for all the members of the family database

import psycopg2
from mainDB import *


#########################################################################
def creditDetails(creditCardDict, creditLineOfCreditDict, creditOtherDict):
	print("**********************************************************************************")
	print("The following section will collect details on your credit limit from all sources")
	print("**********************************************************************************")

	val_creditCard = input("Do you have a credit card? [ yes | no ]  ")
	while ('yes' in val_creditCard):
		val_creditCard_name = input("What is the name of this credit card? [ No spaces ]  ")
		val_creditCard_amount = input("What is the credit limit on this credit card?   ")
		creditCardDict.update({val_creditCard_name: val_creditCard_amount})
		val_creditCard = input("Do you have anymore Credit Cards? [yes | no]  ")
	print("**********************************************************************************")

	val_lineOfCredit = input("Do you have a line of credit? [ yes | no ]  ")
	while ('yes' in val_lineOfCredit):
		val_creditCard_loc_name = input("Which bank do you have this line of credit with? [ No spaces ]  ")
		val_creditCard_loc_amount = input("What is the credit limit on this?   ")
		creditLineOfCreditDict.update({val_creditCard_loc_name: val_creditCard_loc_amount})
		val_lineOfCredit = input("Do you have anymore lines of credit? [ yes | no ]   ")
	print("**********************************************************************************")

	val_otherCredit = input("Do you have any other credit products? [ yes | no ]  ")
	while ('yes' in val_otherCredit):
		val_creditCard_other_name = input("What is the name of this credit product? [ No spaces ]  ")
		val_creditCard_other_amount = input("What is the credit limit on this?   ")
		creditOtherDict.update({val_creditCard_other_name: val_creditCard_other_amount})
		val_otherCredit = input("Do you have any other credit products? [ yes | no ]   ")
	print("**********************************************************************************")

	print(creditCardDict)
	print(creditLineOfCreditDict)
	print(creditOtherDict)

#########################################################################
def creditTableDB(val_tableName, val_userName, dict, type):
	local_cursor = connectToDB()

	# Create table statement
	sqlCreateTable1 = """ CREATE TABLE """ + val_tableName + """_""" + type
	sqlCreateTable2 = """ ( id """ + """ text, """

	key = list(dict.keys())
	lastElement = key[-1]

	part = """  """
	for keys, values in dict.items():
		part12 = keys
		part14 = """ text """
		part_space = """  """
		if (keys == lastElement):
			part13 = """  """
			part = part + part12 + part_space + part14 + part13
		else:
			part13 = """ , """
			part = part + part12 + part_space + part14 + part13

	sqlCreateTable3 = part
	sqlCreateTable4 = """ ); """
	sqlCreateTable = sqlCreateTable1 + sqlCreateTable2 + sqlCreateTable3 + sqlCreateTable4

	# Create a table in PostgreSQL database
	local_cursor.execute(sqlCreateTable)


#########################################################################
def insertValToIdUser_Credit(tableName, val_userName, dict, type):
	local_cursor = connectToDB()
	key = list(dict.keys())
	lastElement = key[-1]

	# Use Update statement so that the same row could be updated
	postgres_insert_query_1T = """ INSERT INTO """ + tableName + """_""" + type + """ ( id, """
	postgres_insert_query_2T = """  """
	postgres_insert_query_3T = """  VALUES ( """ + """ \' """  + val_userName + """ \', """ + """ """
	#postgres_insert_query_4T = """ WHERE id =  """ + val_userName + """ ; """

	# Map keys into Insert Into SQL statement
	for keys in dict:
		part1 = """ = """
		if (keys == lastElement):
			part4 = """ ) """
			postgres_insert_query_2T = postgres_insert_query_2T + keys + part4
		else:
			part4 = """ , """
			postgres_insert_query_2T = postgres_insert_query_2T + keys + part4

	# Map values into Insert Into SQL statement
	part_val = """ \' """
	postgres_insert_query_2TT = """  """
	for keys, values in dict.items():
		if (keys == lastElement):
			part41 = """ \' ); """
			postgres_insert_query_2TT = postgres_insert_query_2TT + part_val + values + part41
		else:
			part41 = """ \', """
			postgres_insert_query_2TT = postgres_insert_query_2TT + part_val + values  + part41

	postgres_insert_query = postgres_insert_query_1T + postgres_insert_query_2T + postgres_insert_query_3T + postgres_insert_query_2TT

	print(postgres_insert_query)
	local_cursor.execute(postgres_insert_query)

#########################################################################
def updateCreditDBOtherUser(tableName, userName, dict, type):
	local_cursor = connectToDB()

	# Alter Table to add more columns
	key = list(otherItemsList.keys())
	lastElement = key[-1]

	# Use Update statement so that the same row could be updated
	postgres_insert_query_1T = """ ALTER TABLE """ + tableName + """_""" + type
	postgres_insert_query_2T = """  """
	postgres_insert_query_3T = """ ADD """
	postgres_insert_query_4T = """ ; """

	for keys in dict:
		type = """ text """
		# space = """  """
		if (keys == lastElement):
			part4 = """  """
			postgres_insert_query_2T = postgres_insert_query_2T + keys + type + part4
		else:
			part4 = """ , """
			postgres_insert_query_2T = postgres_insert_query_2T + keys + type + part4 + postgres_insert_query_3T

	postgres_insert_query = postgres_insert_query_1T + postgres_insert_query_3T + postgres_insert_query_2T + postgres_insert_query_4T
	local_cursor.execute(postgres_insert_query)

	# Update Table with their respective values


#########################################################################
def mapCreditToUser(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict):

	# This will help identify which DB the action should take place in
	creditCard = "creditCard"
	loc = "loc"
	other = "other"

	creditTableDB(val_tableName, val_userName, creditCardDict, creditCard)
	creditTableDB(val_tableName, val_userName, creditLineOfCreditDict, loc)
	creditTableDB(val_tableName, val_userName, creditOtherDict, other)

	insertValToIdUser_Credit(val_tableName, val_userName, creditCardDict, creditCard)
	insertValToIdUser_Credit(val_tableName, val_userName, creditLineOfCreditDict, loc)
	insertValToIdUser_Credit(val_tableName, val_userName, creditOtherDict, other)

