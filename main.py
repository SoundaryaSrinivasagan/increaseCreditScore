# Author: Soundarya Srinivasagan
# Date: October 16th, 2022
# Project: increaseCreditScore
# Version: Version_1
# Description: This script will help the user strategize their income to effectively increase credit score

import psycopg2
from mainDB import *
from creditDB import *
from report import *
from dateDB import *


if __name__ == "__main__":

	print("*************************************************************************************************************")
	print("Welcome to increaseCreditScore")
	print("This program will help the user strategize their credit usage to effectively increase their credit score")
	print("*************************************************************************************************************")

	creditCardDict = {}
	creditLineOfCreditDict = {}
	creditOtherDict = {}
	mainDbDict = {}

	# This will help identify which DB the action should take place in
	creditCard = "creditCard"
	loc = "loc"
	other = "other"

	option = input("""Please choose from the following options: 
	(1) Is this your first time running this program --> Type 1
	(2) Add user to database --> Type 2 
	(3) Configure bill payments --> Type 3 
	(4) Configure credit limits --> Type 4  
	(5) Get updated report --> Type 5 
	(6) Test
	Choice = """)

	# First time running this program
	if ("1" in option):
		val_tableName = input("Please enter your Database Name: ")
		val_userName = input("What is your name: ")
		query_billsCollect(val_tableName, val_userName, True)

		# This will create and add details regarding your credit limit
		creditDetails(creditCardDict, creditLineOfCreditDict, creditOtherDict)
		mapCreditToUser(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict)

		# This will collect information on when the statement is due for each credit that was entered in the section before
		dateDetails(creditCardDict, creditLineOfCreditDict, creditOtherDict)

	# Add user to database
	elif ("2" in option):
		val_tableName = input("Please enter your Database Name: ")
		val_userName = input("What is your name: ")
		query_billsCollect(val_tableName, val_userName, False)

		# Need to have option to add credit information for other users

	# Configure bill payments
	elif ("3" in option):
		print(".............................................................................................")
		print("Please choose from the following:")
		val_option = input("""
		(1) Would you like to add additional credit card bill payments --> Type 1
		(2) Would you like to update your current bill payments --> Type 2 
		Choice = """)

		# Add additional credit card bill payments for existing user
		if ("1" in val_option):
			val_tableName = input("Please enter your Database Name: ")
			val_userName = input("What is your name: ")

			# This will create the columns
			alterTableToAddMoreColumns(val_tableName, val_userName, mainDbDict)

			# Insert values from user into Database (for other payments)
			insertDataDBOtherPayments(val_tableName, val_userName, mainDbDict)

			# Need to add data from this to the table
			dateDetails(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict)


		# Update your current bill payments
		elif ("2" in val_option):
			print("2")

	# Configure credit limits
	elif ("4" in option):
		print(".............................................................................................")
		print("Please choose from the following:")
		val_option = input("""
		(1) Would you like to add additional credit information --> Type 1
		(2) Would you like to update your credit information --> Type 2 
		Choice = """)

		# Add additional credit information
		if ("1" in val_option):
			val_tableName = input("Please enter your Database Name: ")
			val_userName = input("What is your name: ")
			creditDetails(creditCardDict, creditLineOfCreditDict, creditOtherDict)
			mapCreditToUser(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict)

		# Update your credit information
		elif ("2" in val_option):
			val_tableName = input("Please enter your Database Name: ")
			val_userName = input("What is your name: ")
			listResults = printValuesInTable(val_tableName, val_userName)

			count = 1
			for item in listResults:
				print(count, end = ' ')
				print(item)
				count = count + 1
			val_choice = input("Choice = ")

			# Need to configure choice and take out id and make the change reflect onto the DB

	# Get updated report
	elif ("5" in option):
		val_tableName = input("Please enter your Database Name: ")
		val_userName = input("What is your name: ")

		print("Please open report.txt from your current directory")
		reportGenerate(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict)

	elif ("6" in option):
		val_tableName = input("Please enter your Database Name: ")
		val_userName = input("What is your name: ")
		# This will collect information on when the statement is due for each credit that was entered in the section before
		dateDetails(val_tableName, val_userName, creditCardDict, creditLineOfCreditDict, creditOtherDict)


# Other members part of the family can add data to the same DB
## Current problem = the DBs here are empty and you need to Alter and update the table
### Might become easier when you simplify code
# updateCreditDBOtherUser(val_tableName, val_userName, creditCardDict, creditCard)
# updateCreditDBOtherUser(val_tableName, val_userName, creditLineOfCreditDict, loc)
# updateCreditDBOtherUser(val_tableName, val_userName, creditOtherDict, other)
